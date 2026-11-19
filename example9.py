#Program to check the gender of the person in a photo

import base64
from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

with open("Photo2.JPG", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

result = client.decisions.create(
    model="gemini-decision-1",
    input=[
        {"type": "text", "text": "Individual photo of the person"},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg",
            "resolution": "high",  # Supported values: "low", "medium", "high", "ultra_high"
        },
    ],
    questions={
        "gender": {
            "type": "noul",
            "instructions": "Does the photo show the gender of the person?",
        },
        "gender_identified": {
            "type": "choice",
            "instructions": "What is the gender of the person?",
            "criteria": {
                "male": "The person is male.",
                "female": "The person is female.",
            },
        },
    },
)

print(result.answers["gender"].noul)
print(result.answers["gender_identified"].choice)
print("-----------------------------------")
print(result.model_dump_json(indent=4))