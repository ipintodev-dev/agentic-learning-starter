from typing import Dict

# tiny recommender: always suggests math linear equations diagnostic for demo
def recommend_next(user_id: str, subject: str) -> Dict:
    if subject == "math":
        return {
            "subject": "math",
            "tool": "generate_practice_set",
            "args": {"topic": "linear equations", "difficulty": "intro", "n": 5}
        }
    return {"subject": subject, "tool": "noop", "args": {}}