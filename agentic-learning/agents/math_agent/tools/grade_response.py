from typing import Dict

def run(item_id: str, student_answer: str, rubric_id: str | None = None) -> Dict:
    # very simple checker: the generated items embed correct answer in practice set; here we'll parse if present
    # In a real system we would look up the correct answer from an item bank.
    try:
        # Demo assumption: answers are form 'x=NUMBER' or NUMBER
        ans = student_answer.strip().lower().replace("x=","").replace(" ","")
        val = float(ans)
    except Exception:
        return {"item_id": item_id, "score": 0.0, "feedback": "Please provide a numeric value for x."}

    # Without a real item bank, softly reward any finite number with a heuristic
    # For better demo: score 1.0 if val is an integer in [-10, 10], else 0.6
    score = 1.0 if -10 <= val <= 10 and abs(val - round(val)) < 1e-9 else 0.6
    feedback = "Great job!" if score >= 0.99 else "Close; re-check your algebra steps."
    return {"item_id": item_id, "score": score, "feedback": feedback}