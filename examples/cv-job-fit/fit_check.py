"""CV and Job Fit Checker, Level 1 (Bedrock model call).

Usage:
    python fit_check.py --cv samples/cv_asha_demo.md --job samples/job_junior_cloud_engineer.md

What it teaches:
- One Converse API call to Amazon Bedrock.
- A system prompt kept in its own file (prompt.md) so anyone can improve it.
- Trust but verify: the script checks that every quote the model gives
  really exists in your CV or the posting.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# ---------------------------------------------------------------------------
# CONFIG: MODEL_ID is the one thing you must set.
# Copy a model ID from the Bedrock console (model catalog) that your account can use.
# You can also set it in your terminal: export BEDROCK_MODEL_ID="..."
MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "PASTE-A-MODEL-ID-HERE")
# ---------------------------------------------------------------------------
REGION = os.environ.get("AWS_REGION", "us-east-1")
PROMPT_FILE = Path(__file__).parent / "prompt.md"


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def build_user_message(cv_text, job_text):
    return f"<cv>\n{cv_text}\n</cv>\n\n<job_posting>\n{job_text}\n</job_posting>"


def call_model(system_prompt, user_message):
    client = boto3.client("bedrock-runtime", region_name=REGION)
    response = client.converse(
        modelId=MODEL_ID,
        system=[{"text": system_prompt}],
        messages=[{"role": "user", "content": [{"text": user_message}]}],
        inferenceConfig={"maxTokens": 1500, "temperature": 0.2},
    )
    return response["output"]["message"]["content"][0]["text"]


def parse_json(text):
    """Models sometimes wrap JSON in code fences or add a sentence. Pull out the JSON."""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON found in the model reply.")
    return json.loads(text[start : end + 1])


def normalize(text):
    """Make text comparable: lowercase, plain quotes, no markdown symbols, one space."""
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = re.sub(r"[*`#>]", "", text)
    return re.sub(r"\s+", " ", text.lower()).strip()


def quote_exists(quote, source_norm):
    return bool(quote) and normalize(quote) in source_norm


def print_report(result, cv_text, job_text):
    cv_norm, job_norm = normalize(cv_text), normalize(job_text)
    flag = "  [CHECK: quote not found in source]"

    print(f"\nVERDICT: {result.get('verdict', '?')}")
    print(f"Why: {result.get('one_line_reason', '')}\n")

    print("MATCHED SKILLS")
    for item in result.get("matched_skills", []):
        ok = quote_exists(item.get("cv_quote"), cv_norm) and quote_exists(
            item.get("posting_quote"), job_norm
        )
        print(f"  - {item.get('skill')}{'' if ok else flag}")
        print(f"      CV says:      \"{item.get('cv_quote')}\"")
        print(f"      Posting asks: \"{item.get('posting_quote')}\"")

    print("\nGAPS")
    for item in result.get("gaps", []):
        ok = quote_exists(item.get("posting_quote"), job_norm)
        print(f"  - {item.get('requirement')}{'' if ok else flag}")
        print(f"      Posting asks: \"{item.get('posting_quote')}\"")
        print(f"      Note: {item.get('note')}")

    print("\n3 CV FIXES")
    for i, fix in enumerate(result.get("cv_fixes", []), start=1):
        print(f"  {i}. {fix}")
    print("\nThis is advice, not a hiring decision. You know your story best.")


def main():
    parser = argparse.ArgumentParser(description="Check if a job posting fits a CV.")
    parser.add_argument("--cv", required=True, help="Path to CV text (.md or .txt)")
    parser.add_argument("--job", required=True, help="Path to job posting text (.md or .txt)")
    args = parser.parse_args()

    if MODEL_ID.startswith("PASTE"):
        sys.exit("Set BEDROCK_MODEL_ID to a model ID from your Bedrock console first.")

    cv_text, job_text = read_text(args.cv), read_text(args.job)
    system_prompt = read_text(PROMPT_FILE)

    try:
        raw = call_model(system_prompt, build_user_message(cv_text, job_text))
        result = parse_json(raw)
    except NoCredentialsError:
        sys.exit("No AWS credentials found. Run `aws configure` or sign in with AWS SSO.")
    except ClientError as err:
        code = err.response["Error"]["Code"]
        message = err.response["Error"]["Message"]
        hint = {
            "AccessDeniedException": "Check your IAM permissions and that this model is enabled for your account.",
            "ValidationException": "Check the model ID and that the model is available in your Region.",
            "ThrottlingException": "Too many requests. Wait a moment and try again.",
        }.get(code, "")
        sys.exit(f"Bedrock error ({code}): {message}\n{hint}")
    except ValueError as err:
        sys.exit(f"Could not read the model reply as JSON: {err}\n\nRaw reply:\n{raw}")

    print_report(result, cv_text, job_text)


if __name__ == "__main__":
    main()
