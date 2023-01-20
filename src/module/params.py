from os import getenv

PARAMS = {
    "QUEST_URL": getenv("QUEST_URL", "").rstrip('/'),
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": "(" + ",".join([c.strip() for c in getenv("COLUMNS", "").split(",")]) + ")" if getenv("COLUMNS") else None,
    "LABELS": [label.strip() for label in getenv("LABELS", "").split(',')] if getenv("LABELS") else None
}

