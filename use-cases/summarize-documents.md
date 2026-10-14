# Summarize Long Documents

**Contributed by:** @kevintuei (seed use case)

## The problem

People receive long reports, policies, and meeting notes and do not have time to read them. They need the key points and the actions, fast.

## Bedrock piece to reach for

Model call.

## Why that piece

The whole document fits in one request, so there is nothing to look up and no action to take. A Knowledge Base or Agent would add cost and complexity for no gain. If the document is too long for one request, split it into parts and summarize each part first.

## How it works

1. The user pastes or uploads the document text.
2. The model is asked for a summary in a fixed shape, like "5 key points and 3 actions".
3. The user reads a short summary and can ask follow-up questions.

## Watch out for

The model can leave out something important or state something the document never said. For anything that matters, ask for quotes from the document next to each point and check them.
