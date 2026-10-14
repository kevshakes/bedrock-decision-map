# Bedrock Decision Map

**Not sure which part of Amazon Bedrock to use? Start here.**

Built live at the DevJunction webinar "Amazon Bedrock for Beginners" by Kevin Tuei. It is open source, and your first contribution takes about 5 minutes. No AWS account needed to contribute.

---

## Bedrock in four pieces (plain words)

| Piece | What it is | Think of it as |
|---|---|---|
| **Model call** | You send text to a foundation model and get text back | Asking a smart assistant one question |
| **Knowledge Bases** | The model answers using your own documents (this is called RAG) | Giving the assistant your files to read first |
| **Agents** | A model that plans steps and calls tools or APIs that you allow | An assistant that can also do things, not just talk |
| **Guardrails** | Rules that filter what goes in and out, like blocking personal data or off-topic answers | A safety net around the assistant |

Most real apps combine two or more pieces.

## Which piece do I reach for?

1. Do you just need text in and text out? Start with a **Model call**.
2. Must the answers come from your own documents? Add a **Knowledge Base**.
3. Must the bot take actions, like fetching a page or checking an order? Use an **Agent**.
4. Does it touch people's data, or will the public use it? Add **Guardrails**.

## The Decision Map

| Use case | Reach for | Why | Status |
|---|---|---|---|
| [CV and job fit checker](use-cases/cv-job-fit.md) | Model call, then Guardrails, Agent, Knowledge Base | One use case that grows through all four pieces | Level 1 runnable |
| [Summarize long documents](use-cases/summarize-documents.md) | Model call | Text in, short text out. No extra setup | Seed |
| [Customer support bot from FAQs](use-cases/support-bot-from-faqs.md) | Knowledge Base + Guardrails | Answers must come from approved content and stay on topic | Seed |
| [Chat with your own PDFs](use-cases/chat-with-your-pdfs.md) | Knowledge Base | The model needs your documents, not just its training | Seed |
| [Order status or booking assistant](use-cases/order-status-assistant.md) | Agent | It must call a system to look things up or act | Seed |

Your use case belongs here too. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Flagship example: CV and Job Fit Checker

Paste a CV and a job posting. The bot says **Apply**, **Apply with changes**, or **Skip**, and it must quote the CV and the posting as proof. There is no match score on purpose, because a number like "73%" looks precise but is not.

Level 1 is built and runnable in [`examples/cv-job-fit`](examples/cv-job-fit). Levels 2 to 4 are open for you to build.

## Run something in 10 minutes

1. Create an AWS account and **set a budget alert first** (Billing, Budgets). Bedrock is pay per use.
2. Pick a Region where Bedrock is available and open the Bedrock console.
3. In the model catalog, confirm your account can use at least one text model, and copy its **model ID**.
4. Configure credentials on your machine with `aws configure` or AWS SSO. Never paste keys into code or commit them.
5. Install the library: `pip install boto3`
6. Run the starter: `python starter/hello_bedrock.py`

Check the current Bedrock pricing page for rates. Prices and model availability change.

## Contribute

Add a use case, fix a typo, or build one of the roadmap levels. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
