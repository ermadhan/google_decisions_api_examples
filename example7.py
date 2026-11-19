import json
from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

order = {"order": {"id": "8821", "item": "headphones", "price_usd": 240}, "tier": "Gold"}
message = {"message": "Audio cuts out on the left earcup. Fix it today or I cancel my membership."}

result = client.decisions.create(
    model="gemini-decision-1",
    input=[
        {"type": "text", "text": json.dumps(order) + "\n"},
        {"type": "text", "text": json.dumps(message)},
    ],
    questions={
        "is_defect": {
            "type": "noul",
            "instructions": "Does `message` describe a hardware defect?",
        },
        "next_action": {
            "type": "choice",
            "instructions": "What is the right resolution given `tier` and `order`?",
            "criteria": {
                "instant_refund": "Refund without return. Low value or clear fault.",
                "replacement_shipment": "Ship a replacement. Customer returns the original.",
                "troubleshooting_flow": "The issue may be fixable by the customer.",
                "human_escalation": "",
            },
        },
        "churn_risk": {
            "type": "score",
            "instructions": "How likely is the customer to churn if the issue is not resolved now?",
            "criteria": [
                "No churn signal",
                "Mild frustration",
                "Mentions alternatives",
                "Threatens to cancel",
            ],
        },
    },
)

a = result.answers
if a["is_defect"].noul > 0.9 and a["next_action"].confidence > 0.6:
    action = a["next_action"].choice
else:
    action = "human_escalation"

print("Action:", action, "Churn risk score:", a["churn_risk"].score)
print("------------------------------")
print("Full result:", result.model_dump_json(indent=4)) 