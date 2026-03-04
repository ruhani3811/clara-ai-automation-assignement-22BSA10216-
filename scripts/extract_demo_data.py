
import json, sys, re
from pathlib import Path

file_path = sys.argv[1]

with open(file_path) as f:
    text = f.read().lower()

account_id = Path(file_path).stem

data = {
    "account_id": account_id,
    "company_name": "",
    "business_hours": "",
    "office_address": "",
    "services_supported": [],
    "emergency_definition": [],
    "emergency_routing_rules": "",
    "non_emergency_routing_rules": "",
    "call_transfer_rules": "",
    "integration_constraints": "",
    "after_hours_flow_summary": "",
    "office_hours_flow_summary": "",
    "questions_or_unknowns": [],
    "notes": "generated from demo transcript"
}

company = re.search(r'company name is (.*)', text)
if company:
    data["company_name"] = company.group(1)

services = re.findall(r'(sprinkler|alarm|electrical|hvac)', text)
data["services_supported"] = list(set(services))

if "emergency" not in text:
    data["questions_or_unknowns"].append("emergency_definition")

print(json.dumps(data, indent=2))
