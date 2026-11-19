from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

result = client.decisions.create(
    model="gemini-decision-1",
    input=[
        {
            "type": "video",
            "uri": "https://storage.googleapis.com/generativeai-downloads/videos/ForBiggerBlazes.mp4",
            "mime_type": "video/mp4",
            "resolution": "low",
        },
    ],
    questions={
        "shows_fire": {
            "type": "noul",
            "instructions": "Does the video show fire or flames?",
        },
    },
)

print("Shows fire:", result.answers["shows_fire"].noul)
print("-----------------------------------")
print("Full result:", result.model_dump_json(indent=4))