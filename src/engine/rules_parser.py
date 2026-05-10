# Rule parser stub
# In future, parse PDF or JSON

def load_rules():
    import json
    with open('rules/core_rules.json') as f:
        return json.load(f)

print('Rules loaded successfully for Phase 1')
