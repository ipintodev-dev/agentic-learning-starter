from typing import List, Dict
import random

def run(topic: str, difficulty: str, n: int, standards: List[str] | None = None) -> Dict:
    items = []
    for i in range(n):
        qid = f"ALG.LIN1.Q{i+1}"
        a = random.randint(1,9)
        b = random.randint(1,9)
        c = a * random.randint(1,9) + b  # ensures integer solution
        # ax + b = c -> x = (c - b)/a
        prompt = f"Solve for x: {a}x + {b} = {c}"
        solution = (c - b) / a
        items.append({"item_id": qid, "prompt": prompt, "answer": solution, "topic": topic, "difficulty": difficulty})
    return {"items": items}