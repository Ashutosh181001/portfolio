# Project 01 — Agent From Scratch vs. LangChain

## The idea

Before I lean on any framework, I want to actually understand what it's doing for me. So the plan here is simple: build a small AI agent completely from scratch — no LangChain, no orchestration library, just an LLM call, a loop, and some mock tools — and get it to reason about a task, decide to call a tool, and return a result.

Then I'll build the *same* thing again using LangChain, and put them side by side.

## What I'm comparing

- **Complexity** — how much code, how many abstractions, how much do I actually need to understand to make each version work?
- **Speed** — does the extra framework machinery add noticeable latency, or does it pay for itself?
- **Developer experience** — what does the framework buy me, and what does it hide from me?

## Why mock tools

I want to isolate "how does an agent decide and act" from "is this real API flaky/slow/costly today." Mock tools return deterministic, made-up results so both versions can be compared fairly and repeatably.

## Status

Just getting started — this README is step one. Code, notes, and a writeup of what I learn will land here as I go.
