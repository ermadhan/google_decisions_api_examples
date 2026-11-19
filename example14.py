from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input="I need to give car to service center which is 100 metres from my house.",
    questions={
        "intention_valid": {
            "type": "choice",
            "instructions": "Should owner drive or walk?",
            "criteria": {
                "walking": "Owner walks to drop the car",
                "driving": "Owner drives to drop the car.",
            },
        },
    },
)

print("Full result:", result.to_json())
print("------------------------------")
answer = result.answers["intention_valid"]
print("Intention valid score:", f"P={answer.choice} confidence={answer.confidence:.2f}")