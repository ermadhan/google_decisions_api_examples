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

print(result.model_dump_json(indent=4))
answer = result.answers["department"]
print(answer.choice, answer.confidence, answer.probabilities)