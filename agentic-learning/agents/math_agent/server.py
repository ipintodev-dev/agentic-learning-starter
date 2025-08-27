from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.math_agent.tools import generate_practice_set, explain_concept, grade_response

http_app = FastAPI(title="Math Subject Agent (HTTP fallback)", version="0.1.0")

class GenerateBody(BaseModel):
    topic: str
    difficulty: str
    n: int
    standards: list[str] | None = None

class ExplainBody(BaseModel):
    concept_id: str
    learner_context: dict | None = None

class GradeBody(BaseModel):
    item_id: str
    student_answer: str
    rubric_id: str | None = None

@http_app.post("/tools/generate_practice_set")
def generate(body: GenerateBody):
    try:
        return generate_practice_set.run(**body.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@http_app.post("/tools/explain_concept")
def explain(body: ExplainBody):
    try:
        return explain_concept.run(**body.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@http_app.post("/tools/grade_response")
def grade(body: GradeBody):
    try:
        return grade_response.run(**body.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))