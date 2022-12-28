from os import getenv

PARAMS = {
    "QUEST_URL": getenv("QUEST_URL", ""),
    "TABLE_NAME": getenv("TABLE_NAME", ""),
    "COLUMNS": getenv("COLUMNS", ""),
    "LABELS": getenv("LABELS", "")
}

# remove path indicator just to clean-up URL
if PARAMS['QUEST_URL'][-1] == '/':
    PARAMS['QUEST_URL'] = PARAMS['QUEST_URL'][:-1]

# parse columns and labels
if PARAMS['COLUMNS']:
    PARAMS['COLUMNS'] = [header.strip() for header in PARAMS['COLUMNS'].split(',')]
else:
    PARAMS['COLUMNS'] = None

if PARAMS['LABELS']:
    PARAMS['LABELS'] = [header.strip() for header in PARAMS['LABELS'].split(',')]
else:
    PARAMS['LABELS'] = None
