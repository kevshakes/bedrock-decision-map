# CV and Job Fit Checker

A bot that reads a CV (or portfolio text) and a job posting, then tells you if the opportunity is relevant for **that** CV.

- **Level 1 (model call):** built and runnable here.
- **Levels 2 to 4:** open roadmap. Pick one and send a PR.

## What the output looks like

- A verdict: **Apply**, **Apply with changes**, or **Skip**
- Matched skills, each with a quote from the CV and a quote from the posting
- Gaps, each with a quote from the posting
- Three concrete CV fixes

## Design rules (please keep these when you contribute)

1. **Evidence only.** Every claim quotes the CV or the posting. The script checks that the quotes are real and flags any that are not.
2. **No match score.** A number like "73%" looks precise but is not, and it biases people.
3. **Ignore protected traits.** Name, gender, age, tribe, nationality, religion, photo, and school prestige must not affect the verdict.
4. **Honest fixes.** The bot may reword or surface what is true. It must never suggest inventing skills.
5. **Documents are data, not instructions.** See the injection test below.

## Run Level 1

```bash
pip install -r requirements.txt

# Copy a model ID from your Bedrock console (model catalog)
export BEDROCK_MODEL_ID="paste-your-model-id"
export AWS_REGION="us-east-1"   # use a Region where Bedrock is available to you

python fit_check.py --cv samples/cv_asha_demo.md --job samples/job_junior_cloud_engineer.md
```

Then try the other posting and compare:

```bash
python fit_check.py --cv samples/cv_asha_demo.md --job samples/job_senior_data_scientist.md
```

Expected: the first posting is a fit (Apply or Apply with changes). The second should be **Skip**.

### Injection test

`samples/cv_injection_test.md` hides an instruction that tries to force an "Apply" verdict.

```bash
python fit_check.py --cv samples/cv_injection_test.md --job samples/job_junior_cloud_engineer.md
```

A good run ignores the hidden instruction and returns **Skip**. If yours does not, improve `prompt.md` and send a PR.

### Use your own CV safely

Copy your CV as plain text into a `private/` folder. That folder is in `.gitignore` so it is never committed. Only use your own CV or one you have permission to use.

## Roadmap

| Level | Task | Bedrock piece | Difficulty |
|---|---|---|---|
| 2 | Add a Guardrail that masks personal details (emails, phone numbers, addresses) before the model sees the CV | Guardrails | Medium |
| 2 | Add a Guardrail denied topic so the bot refuses to rank or reject other people | Guardrails | Medium |
| 3 | Fetch a portfolio URL and a job posting URL so users do not paste text | Agent, or tool use in the Converse API | Hard |
| 4 | Create a role skills ladder (for example junior cloud engineer) and judge the CV against it | Knowledge Base | Hard |
| Any | Support PDF and DOCX CVs | None | Easy |
| Any | Add a `tests/` folder that checks the quote verification logic | None | Easy |
| Any | Add a second sample CV and posting from a non-cloud field | None | Easy |

### Hints for the next levels

- **Level 2:** the Converse call accepts a `guardrailConfig` with a guardrail ID and version. Create the guardrail in the console first, then pass it in `fit_check.py`.
- **Level 3:** start with tool use in the Converse API, where you define a `fetch_page` tool and run it in Python. Move to a Bedrock Agent with an action group once that works.
- **Level 4:** write your skills ladder as plain text files, add them to a Knowledge Base, and retrieve the relevant part before judging the CV.

## Fairness note

This bot gives advice to a candidate about their own CV. It is **not** a tool for employers to screen or reject applicants. Hiring decisions affect real lives and need human judgment.
