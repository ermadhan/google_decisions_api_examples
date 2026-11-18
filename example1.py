from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input=[
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/audio/rehearsing.wav",
            "mime_type": "audio/wav",
        },
    ],
    questions={
        "mentions_launch": {
            "type": "noul",
            "instructions": "Is the speaker talking about a product campaign launch?",
        },
        "delivery": {
            "type": "score",
            "instructions": "How fluent and prepared does the speaker sound?",
            "criteria": [
                "Hesitant, searching for notes, or self-correcting.",
                "Mostly steady with minor pauses.",
                "Polished, fluent, and confident throughout.",
            ],
        },
    },
)

print("mentions_launch:", result.answers["mentions_launch"].noul, "delivery:", result.answers["delivery"].score)