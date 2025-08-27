from typing import Dict

def run(concept_id: str, learner_context: Dict | None = None) -> Dict:
    text = (
        "Linear equations have the form ax + b = c. To solve, isolate x by subtracting b and dividing by a."
    )
    steps = ["Subtract b from both sides", "Divide both sides by a"]
    return {"concept_id": concept_id, "explanation": text, "steps": steps}