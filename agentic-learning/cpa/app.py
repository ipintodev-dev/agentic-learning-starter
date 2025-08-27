from fastapi import FastAPI, HTTPException
from cpa.models.schemas import StartSession, RecommendationRequest, SubmitRequest, ProfileOut
from cpa.recommender import recommend_next
from cpa.mastery import get_mastery, update_mastery, mastery as _store
from cpa.scheduler import due_items
from cpa.mcp_client import SubjectAgentClient

app = FastAPI(title="Control Plane Agent (CPA)", version="0.1.0")
client = SubjectAgentClient()

@app.post("/v1/sessions")
def start_session(body: StartSession):
    # For demo, we don't persist sessions; return simple ack
    return {"session_id": f"s_{body.user_id}", "locale": body.locale}

@app.post("/v1/recommendations")
async def recommendations(body: RecommendationRequest):
    plan = recommend_next(body.user_id, body.subject)
    try:
        if plan["tool"] == "generate_practice_set":
            resp = await client.call_tool(body.subject, plan["tool"], plan["args"])
            return {"plan": plan, "items": resp.get("items", [])}
        return {"plan": plan}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

@app.post("/v1/submit")
async def submit(body: SubmitRequest):
    # naive: call grade_response on the agent and update mastery keyed by concept
    try:
        grading = await client.call_tool(body.subject, "grade_response", {
            "item_id": body.item_id,
            "student_answer": body.student_answer
        })
        # pretend concept is derivable from item prefix
        concept_id = body.item_id.rsplit(".", 1)[0]
        delta = 0.1 if grading.get("score", 0) >= 0.7 else -0.05
        new_m = update_mastery(body.user_id, concept_id, delta)
        return {"grading": grading, "concept_id": concept_id, "new_mastery": new_m}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

@app.get("/v1/profiles/{user_id}")
def profile(user_id: str) -> ProfileOut:
    # expose a snapshot of mastery store filtered by user
    filtered = {c: m for (u, c), m in _store.items() if u == user_id}
    return ProfileOut(user_id=user_id, mastery=filtered)