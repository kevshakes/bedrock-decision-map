# Contributing

Welcome. This repo is built for first-time contributors. If you have never opened a pull request, you are in the right place.

## Your first PR in 5 minutes (no Git install needed)

1. Open the [`use-cases`](use-cases) folder on GitHub.
2. Click **Add file**, then **Create new file**.
3. Name it like `your-idea.md` using lowercase words and dashes.
4. Copy everything from [`use-cases/_TEMPLATE.md`](use-cases/_TEMPLATE.md) and paste it in.
5. Fill in each section in plain words. Short is fine.
6. Click **Commit changes**. Choose **Create a new branch** and click **Propose changes**.
7. Click **Create pull request**.

That is it. A maintainer will review it and may ask for small edits.

Not ready for a PR? Open an issue with the **Use case idea** form instead.

## What makes a good use case

- It solves a real problem for a real person.
- It names the Bedrock piece to reach for (Model call, Knowledge Base, Agent, or Guardrails) and says why.
- It explains how it works in three simple steps.
- It names one thing to watch out for, like cost, privacy, or wrong answers.

## Ground rules

- **No secrets.** Never commit AWS keys, tokens, or `.env` files.
- **No real personal data.** Use fictional CVs, names, and documents only.
- **Plain language.** If you use a term like RAG, explain it once.
- **One use case per PR.** Small PRs get reviewed faster.
- **Be kind.** Everyone here is learning.

## Building code contributions

Look for issues labelled `good first issue` and `help wanted`. The CV and Job Fit roadmap in [`examples/cv-job-fit/README.md`](examples/cv-job-fit/README.md) lists open levels you can pick up.

Before you open a code PR:

- Run the script on the sample files and show the output in the PR description.
- Keep the model ID as a config value. Do not hardcode one.
- Do not add dependencies unless you need them.
