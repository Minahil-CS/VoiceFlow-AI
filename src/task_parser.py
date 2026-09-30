import re
from datetime import datetime

PRIORITIES = {"high", "medium", "low"}

def parse_task(text: str):
    """Lightweight local parser for a hackathon demo."""
    clean = (text or "").strip()
    lower = clean.lower()

    priority = "medium"
    for p in PRIORITIES:
        if p in lower:
            priority = p
            break

    date_hint = None
    for phrase in ["tomorrow", "today", "friday", "monday", "tuesday",
                   "wednesday", "thursday", "saturday", "sunday"]:
        if phrase in lower:
            date_hint = phrase
            break

    task = re.sub(r"\b(high|medium|low)\s*priority\b", "", clean, flags=re.I)
    task = re.sub(r"\b(today|tomorrow)\b", "", task, flags=re.I)
    task = re.sub(r"\b(on|at)\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b", "", task, flags=re.I)
    task = re.sub(r"\s+", " ", task).strip(" .,!?")

    return {
        "task": task or clean,
        "priority": priority,
        "due_hint": date_hint
    }
