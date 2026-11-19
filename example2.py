from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input="The blue mug I ordered on Monday arrived cracked on Wednesday.",
    questions={
        "is_damaged": {
            "type": "noul",
            "instructions": "Did the item arrive damaged?",
        },
    },
)

print("Full result:", result.to_json())
print("------------------------------")
answer = result.answers["is_damaged"]
print("Is damaged score:", f"P(yes)={answer.noul:.2f} confidence={answer.confidence:.2f}")