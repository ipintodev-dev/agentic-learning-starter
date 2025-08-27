# Agentic Learning (MCP) – Starter Repo

This starter packs a **Control Plane Agent (CPA)** in FastAPI and a **Math Subject Agent** with an **MCP-friendly** layout.
It includes a simple **HTTP fallback** for local testing, while leaving room to wire up a true MCP transport later.

## Contents
- `cpa/` – FastAPI Control Plane (personalization, simple mastery/rec/schedule stubs)
- `agents/math_agent/` – Math agent with tool endpoints and MCP-style structure
- `schemas/` – JSON Schemas for tool contracts
- `scripts/` – helper scripts
- `docker-compose.yml` – quick local orchestration
- `README.md` – this file

## Quick Start (Local, HTTP fallback)

### 1) Create and activate a venv
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2) Install deps (CPA + Agent)
```bash
pip install -r cpa/requirements.txt
pip install -r agents/math_agent/requirements.txt
```

### 3) Start the Math Agent (HTTP mode)
```bash
# default HTTP port: 8081
uvicorn agents.math_agent.server:http_app --reload --port 8081
```

### 4) Start the Control Plane
```bash
# points CPA to the HTTP agent for ease of use
export MATH_AGENT_HTTP_URL=http://localhost:8081
uvicorn cpa.app:app --reload --port 8000
```

### 5) Try it
```bash
# Create a session
curl -s -X POST http://localhost:8000/v1/sessions -H "Content-Type: application/json" -d '{"user_id":"u_1","locale":"he-IL"}' | jq

# Request recommendations (diagnostic -> practice set)
curl -s -X POST http://localhost:8000/v1/recommendations -H "Content-Type: application/json" -d '{"user_id":"u_1","subject":"math"}' | jq

# Submit an answer (fake example)
curl -s -X POST http://localhost:8000/v1/submit -H "Content-Type: application/json" -d '{"user_id":"u_1","subject":"math","item_id":"ALG.LIN1.Q1","student_answer":"x=3"}' | jq

# Inspect profile
curl -s http://localhost:8000/v1/profiles/u_1 | jq
```

## True MCP wiring (optional next step)
This repo stubs a minimal `mcp_client.py` and an MCP-friendly agent tree. To wire a real MCP transport (stdio/websocket/pipe),
use the emerging **Model Context Protocol** tooling (Python package `mcp`, or your chosen SDK). Replace the HTTP fallback calls
with MCP `call_tool` requests and register tool schemas from `agents/math_agent/schemas/`.

## Project Tree
```
agentic-learning/
├─ README.md
├─ docker-compose.yml
├─ LICENSE
├─ .env.example
├─ cpa/
│  ├─ app.py
│  ├─ mcp_client.py
│  ├─ recommender.py
│  ├─ scheduler.py
│  ├─ mastery.py
│  ├─ models/schemas.py
│  ├─ config.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ agents/
│  └─ math_agent/
│     ├─ server.py
│     ├─ tools/
│     │  ├─ generate_practice_set.py
│     │  ├─ explain_concept.py
│     │  └─ grade_response.py
│     ├─ prompts/system.txt
│     ├─ schemas/
│     │  ├─ generate_practice_set.json
│     │  ├─ explain_concept.json
│     │  └─ grade_response.json
│     ├─ requirements.txt
│     └─ Dockerfile
├─ schemas/
│  └─ event.schema.json
└─ scripts/
   ├─ client_demo.py
   └─ run_all.sh
```