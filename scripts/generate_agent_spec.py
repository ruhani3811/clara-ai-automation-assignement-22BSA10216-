
import json, sys

memo_path = sys.argv[1]

with open(memo_path) as f:
    memo = json.load(f)

agent = {
    "agent_name": memo.get("company_name","Unknown") + " AI Assistant",
    "voice_style": "professional",
    "version": "v1",
    "key_variables": {
        "timezone": "unknown",
        "business_hours": memo.get("business_hours",""),
        "office_address": memo.get("office_address","")
    },
    "system_prompt": f"""
You are the phone assistant for {memo.get('company_name','the company')}.

BUSINESS HOURS FLOW
1 greet caller
2 ask purpose
3 collect name and phone
4 transfer call
5 if transfer fails apologize and promise followup

AFTER HOURS FLOW
1 greet caller
2 ask purpose
3 confirm if emergency
4 if emergency collect name phone and address immediately
5 attempt transfer
6 if transfer fails promise urgent callback
"""
}

print(json.dumps(agent, indent=2))
