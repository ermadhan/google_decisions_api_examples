from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input="Export fails in Safari but works in Chrome.",
    questions={
        "severity": {
            "type": "score",
            "instructions": "How severe is this issue for the user?",
            "criteria": [
                "Cosmetic: appearance only, no lost functionality.",
                "Workaround available: a task fails, but another way works.",
                "Fully blocked: a task fails with no workaround.",
            ],
        },
    },
)

answer = result.answers["severity"]
print("Answer score, confidence, probabilities:", answer.score, answer.confidence, answer.probabilities)
print("------------------------------")
print("Full result:", result.model_dump_json(indent=4))
print("------------------------------")
level = max(answer.probabilities, key=answer.probabilities.get)  # "1"
print("Answer legend for level", level, ":", answer.legend[level])  # "Workaround available: ..."