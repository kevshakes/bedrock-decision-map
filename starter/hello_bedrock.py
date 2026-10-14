"""Hello Bedrock: your first model call in about 20 lines.

SETUP CHECKLIST (do these once)
1. Set a budget alert in AWS Billing before you start. Bedrock is pay per use.
2. Pick a Region where Bedrock is available and use it in the console and here.
3. In the Bedrock console, open the model catalog. Confirm your account can use a
   text model and copy its model ID. Some models need access to be requested first.
4. Configure credentials with `aws configure` or AWS SSO. Never put keys in code.
5. Your IAM user or role needs permission to call Bedrock (bedrock:InvokeModel).
6. pip install boto3
7. Run: python starter/hello_bedrock.py
"""
import os

import boto3

# CONFIG: set these as environment variables, or edit the defaults.
MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "PASTE-A-MODEL-ID-HERE")
REGION = os.environ.get("AWS_REGION", "us-east-1")

if MODEL_ID.startswith("PASTE"):
    raise SystemExit("Set BEDROCK_MODEL_ID to a model ID from your Bedrock console.")

client = boto3.client("bedrock-runtime", region_name=REGION)

response = client.converse(
    modelId=MODEL_ID,
    messages=[
        {
            "role": "user",
            "content": [{"text": "Explain Amazon Bedrock to a beginner in 3 sentences."}],
        }
    ],
    inferenceConfig={"maxTokens": 300},
)

print(response["output"]["message"]["content"][0]["text"])
