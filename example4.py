from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input="I was charged twice for my order.",
    questions={
        "department": {
            "type": "choice",
            "instructions": "Which department should handle this request?",
            "criteria": {
                "billing": "Payments, invoices, and refunds.",
                "technical": "Problems using the product.",
                "shipping": "Delivery and tracking.",
                "other": "Anything outside these categories.",
            },
        },
    },
)

print("Full result:", result.model_dump_json(indent=4))
print("------------------------------")
answer = result.answers["department"]
print("Department choice:", answer.choice, "Confidence:", answer.confidence, "Probabilities:", answer.probabilities)