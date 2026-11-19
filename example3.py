from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input="Customer returned the sweater because they preferred green over blue.",
    questions={
        "is_defect": {
            "type": "noul",
            "instructions": "Is the customer reporting a product defect?",
            "criteria": {
                "true_description": "The product itself is broken or faulty.",
                "false_description": "Preference, sizing, shipping, or pricing complaint.",
            },
        },
    },
)

print("Full result:", result.to_json())
print("------------------------------")
print("Is defect score:", result.answers["is_defect"].noul)