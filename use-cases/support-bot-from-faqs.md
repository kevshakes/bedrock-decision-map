# Customer Support Bot From FAQs

**Contributed by:** @kevintuei (seed use case)

## The problem

A small business gets the same questions every day, like opening hours, delivery times, and return rules. Staff spend hours repeating answers, and customers wait.

## Bedrock piece to reach for

Knowledge Base plus Guardrails.

## Why that piece

A plain model call would guess answers from general knowledge, and a wrong delivery promise costs real money. A **Knowledge Base** makes the bot answer from the business's own approved FAQs. **Guardrails** keep it on topic and stop it from collecting or repeating personal data.

## How it works

1. The business uploads its FAQ and policy documents to a Knowledge Base.
2. A customer asks a question. The bot finds the matching FAQ text and answers from it.
3. Guardrails block off-topic requests and personal data. If the answer is not in the FAQs, the bot hands over to a human.

## Watch out for

The bot must say "I don't know" and hand over to a person when the FAQs do not cover the question. Test this on purpose with questions that are not in your documents.
