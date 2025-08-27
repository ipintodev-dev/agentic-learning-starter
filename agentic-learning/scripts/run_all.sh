#!/usr/bin/env bash
set -euo pipefail
export MATH_AGENT_HTTP_URL=${MATH_AGENT_HTTP_URL:-http://localhost:8081}

# Start math agent
echo "Starting Math Agent on :8081 ..."
uvicorn agents.math_agent.server:http_app --port 8081 &
AGENT_PID=$!

# Start CPA
echo "Starting CPA on :8000 ..."
uvicorn cpa.app:app --port 8000 &
CPA_PID=$!

echo "CPA PID: $CPA_PID | Agent PID: $AGENT_PID"
echo "Press Ctrl+C to stop both."

wait