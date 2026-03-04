
# Clara AI Automation Pipeline

This repository demonstrates a zero-cost automation pipeline that converts demo
and onboarding call transcripts into structured configuration files for a Retell AI agent.

## Architecture

Demo Transcript
→ Extraction Script
→ Account Memo JSON
→ Agent Spec Generator
→ Stored Outputs

Onboarding Transcript
→ Update Script
→ Memo v2
→ Agent Spec v2
→ Changelog

## Tech Stack
Python
n8n (local)
Docker
JSON storage

## Setup

1 Install Python
2 Install Docker
3 Place transcripts inside dataset folder
4 Run scripts/run_batch.py

## Output Location

outputs/accounts/<account_id>/

Includes:
memo.json
agent_spec.json
changelog.md

## Improvements
LLM extraction
dashboard
database storage
