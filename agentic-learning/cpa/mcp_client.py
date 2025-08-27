"""
mcp_client.py: optional MCP wiring.
For now, this file only contains an interface + HTTP fallback helper.
Replace HTTP calls with real MCP client calls as you integrate MCP.
"""
from typing import Any, Dict
import os, httpx
from tenacity import retry, stop_after_attempt, wait_exponential

class SubjectAgentClient:
    def __init__(self, http_url_env: str = "MATH_AGENT_HTTP_URL"):
        self.http_url = os.getenv(http_url_env)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.2, min=0.5, max=2.0))
    async def call_tool(self, subject: str, tool: str, args: Dict[str, Any]) -> Dict[str, Any]:
        if self.http_url:
            # Fallback: call HTTP tool on math agent
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.post(f"{self.http_url}/tools/{tool}", json=args)
                resp.raise_for_status()
                return resp.json()
        # Placeholder for true MCP invocation
        raise RuntimeError("No HTTP fallback configured and MCP not yet wired.")