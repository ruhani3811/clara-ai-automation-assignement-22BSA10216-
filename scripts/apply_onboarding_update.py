
import json, sys

memo_path = sys.argv[1]
onboarding_text = sys.argv[2]

with open(memo_path) as f:
    memo = json.load(f)

changes = []

if "24/7" in onboarding_text:
    memo["business_hours"] = "24/7"
    changes.append("business_hours updated to 24/7")

if "fire alarm" in onboarding_text:
    memo.setdefault("emergency_definition",[]).append("fire alarm triggered")
    changes.append("added fire alarm emergency")

print(json.dumps({"updated_memo": memo, "changes": changes}, indent=2))
