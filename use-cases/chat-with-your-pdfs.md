# Chat With Your Own PDFs

**Contributed by:** @kevintuei (seed use case)

## The problem

Students and professionals have piles of notes, papers, and manuals. Searching them by keyword misses the answer when the wording differs.

## Bedrock piece to reach for

Knowledge Base (RAG).

## Why that piece

The model has never seen your private documents. RAG (retrieval augmented generation) means the system first finds the most relevant passages in your files, then gives them to the model to answer from. This is exactly what a **Knowledge Base** does for you, so you do not build the search part yourself.

## How it works

1. Your PDFs are stored and indexed in a Knowledge Base.
2. You ask a question in normal language.
3. The system retrieves the best passages and the model answers using them, with a pointer to the source.

## Watch out for

Scanned PDFs with poor text quality give poor answers. Always check the cited source passage before trusting an answer. Storage and search have their own costs, so read the current pricing and delete test setups when you are done.
