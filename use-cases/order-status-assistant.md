# Order Status or Booking Assistant

**Contributed by:** @kevintuei (seed use case)

## The problem

Customers want to ask "where is my order?" or "book me a slot for Friday" in normal language. Answering needs live data from a system, and booking means taking an action.

## Bedrock piece to reach for

Agent.

## Why that piece

A model call cannot look up an order, and a Knowledge Base only holds documents. An **Agent** can decide which tool to use, call your API or function, read the result, and reply. You decide which actions it is allowed to take.

## How it works

1. The customer asks a question in plain language.
2. The agent picks an allowed action, like "get order status", and calls it with the order number.
3. The agent reads the result and replies in a friendly way.

## Watch out for

Give the agent the smallest set of actions it needs. Read-only actions are safe to start with. Ask the customer to confirm before any action that changes something, like a booking or a cancellation.
