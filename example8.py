import base64
from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

with open("Ticket.pdf", "rb") as f:
    pdf_b64 = base64.b64encode(f.read()).decode("utf-8")

result = client.decisions.create(
    model="gemini-decision-1",
    input=[
        {
            "type": "document",
            "data": pdf_b64,
            "mime_type": "application/pdf",
        },
    ],
    questions={
        "ticket_QR_Code": {
            "type": "noul",
            "instructions": "Does the ticket include a QR code?",
        },
        "travel_itinerary": {
            "type": "choice",
            "instructions": "Which travel itinerary fits this ticket?",
            "criteria": {
                "dates": "Bus details including date of travel and times.",
                "places": "pickup and dropping points.",
                "passenger": "Passenger details including name and contact information .",
                "fare": "Fare details.",
            },
        },
    },
)

po = result.answers["ticket_QR_Code"]
category = result.answers["travel_itinerary"]
print(po.noul, category.choice, category.confidence)
print("-----------------------------------")
print(result.model_dump_json(indent=4))