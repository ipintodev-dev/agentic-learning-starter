from typing import Dict, Tuple

# super-naive in-memory mastery store for demo
# mastery[(user_id, concept_id)] -> float  (0..1)
mastery: Dict[Tuple[str, str], float] = {}

def get_mastery(user_id: str, concept_id: str) -> float:
    return mastery.get((user_id, concept_id), 0.3)  # default low mastery

def update_mastery(user_id: str, concept_id: str, delta: float) -> float:
    m = mastery.get((user_id, concept_id), 0.3)
    m = max(0.0, min(1.0, m + delta))
    mastery[(user_id, concept_id)] = m
    return m