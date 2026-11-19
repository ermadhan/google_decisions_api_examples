from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input="I need to give car to service center which is 100 metres from my house. I am planning to walk to the service center to drop the car.",
    #input="I need to give my car to service center which is 100 metres from house. I am planning to walk to the service center to drop the car.",
    #input="I need to give my car to service center which is 100 metres from house. I am planning to walk to the service center.",
    questions={
        "intention_valid": {
            "type": "choice",
            "instructions": "Is the owner intention valid?",
            "criteria": {
                "yes": "The owner's intention is valid.",
                "no": "The owner's intention is not valid.",
            },
        },
    },
)

print("Full result:", result.to_json())
print("------------------------------")
answer = result.answers["intention_valid"]
print("Intention valid score:", f"P(yes)={answer.choice} confidence={answer.confidence:.2f}")