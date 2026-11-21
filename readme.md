# Google Decisions API Examples

A comprehensive collection of practical examples demonstrating how to use the **Google Decisions API** (`gemini-decision-1`) using the official `google-genai` SDK in Python.

- **Decisions API Documentation**: [https://aistudio.google.com/docs/decisions-api](https://aistudio.google.com/docs/decisions-api)
- **API Reference**: [https://aistudio.google.com/api-reference](https://aistudio.google.com/api-reference)

---

## Overview

The **Google Decisions API** provides calibrated, structured decision-making on top of Gemini models (`gemini-decision-1`). Rather than generating open-ended text, it evaluates questions against an input context and returns calibrated probabilities, confidence scores, and categorical answers.

### Key Capabilities
- **Multimodal Context Support**: Evaluate decisions over text, audio, images, videos, and documents (PDF).
- **Multiple Questions per Request**: Run batch questions concurrently against the shared input context.
- **Calibrated Scores & Probabilities**: Receive true probability distributions $\in [0, 1]$ and confidence metrics instead of arbitrary text responses.
- **Rule-based & Programmatic Guardrails**: Integrate confidence thresholds directly into downstream deterministic logic and workflows.

---

## Core Question Types

The Decisions API supports three primary question types:

| Question Type | Output Type | Description | Result Attributes |
|---|---|---|---|
| **`noul`** | Binary / Boolean | Evaluates a binary hypothesis (yes/no, true/false). Returns a calibrated probability $P(\text{true}) \in [0, 1]$. | `answer.noul`<br>`answer.confidence` |
| **`choice`** | Categorical | Single-select choice across 2 to 255 mutually exclusive options. | `answer.choice`<br>`answer.confidence`<br>`answer.probabilities` |
| **`score`** | Ordinal Scale | Evaluates input along an ordered rubric scale (e.g., 1–3, 1–5). | `answer.score`<br>`answer.confidence`<br>`answer.probabilities`<br>`answer.legend` |

### Question Criteria Guidelines
- **`noul`**: Optional criteria can be defined using `true_description` and `false_description`:
  ```python
  "criteria": {
      "true_description": "The product itself is broken or faulty.",
      "false_description": "Preference, sizing, shipping, or pricing complaint.",
  }
  ```
- **`choice`**: Criteria maps each option ID to its description:
  ```python
  "criteria": {
      "billing": "Payments, invoices, and refunds.",
      "technical": "Problems using the product.",
      "shipping": "Delivery and tracking.",
  }
  ```
- **`score`**: Criteria is an ordered list representing each score level:
  ```python
  "criteria": [
      "Low severity: minor cosmetic issue.",
      "Medium severity: workaround exists.",
      "High severity: blocker with no workaround.",
  ]
  ```

---

## Supported Input Modalities

The `input` parameter accepts strings, structured JSON dictionaries, or multimodal content lists:

1. **Text**: Raw string, list of strings, or serialized JSON (e.g., tickets, chat logs).
2. **Audio**: GCS URIs or base64 data (`audio/wav`, `audio/mp3`).
3. **Image**: Base64 encoded images (`image/jpeg`, `image/png`) with optional resolution levels (`"low"`, `"medium"`, `"high"`, `"ultra_high"`).
4. **Video**: URIs or base64 data (`video/mp4`) with resolution settings.
5. **Document**: Base64 encoded PDFs (`application/pdf`).

---

## Examples Catalog

| File | Modality | Question Types | Description |
|---|---|---|---|
| `example1.py` | Audio (`audio/wav` URI) | `noul`, `score` | Evaluates speaker fluency (`score` rubric) and checks whether a product campaign launch is mentioned (`noul`). |
| `example2.py` | Text | `noul` | Basic binary classification: determines whether a customer received a damaged item, reading probability and confidence. |
| `example3.py` | Text | `noul` | Demonstrates custom `noul` criteria using `true_description` and `false_description` to distinguish defects from return preferences. |
| `example4.py` | Text | `choice` | Support ticket categorization (`billing`, `technical`, `shipping`, `other`) inspecting winning choice, confidence, and probability distribution. |
| `example5.py` | Text | `score` | Issue severity triage on a 3-tier ordinal rubric; retrieves winning score, probability distribution, and rubric `legend`. |
| `example6.py` | Compound Text / JSON | `noul`, `choice`, `score` | Customer service workflow combining order details and message: assesses defect presence, chooses next action, estimates churn risk, and applies routing thresholds. |
| `example7.py` | Compound Text / JSON | `noul`, `choice`, `score` | Multi-criteria automated customer support escalation with full JSON response serialization. |
| `example8.py` | Document (`application/pdf`) | `noul`, `choice` | Ingests a base64-encoded PDF ticket, checks for the presence of a QR code (`noul`), and classifies the travel itinerary details (`choice`). |
| `example9.py` | Image (`image/jpeg`) | `noul`, `choice` | High-resolution image analysis checking whether gender is visible (`noul`) and identifying person gender (`choice`). |
| `example10.py` | Audio (`audio/wav` URI) | `noul`, `score` | Remote audio speech evaluation testing speaker delivery quality and message content. |
| `example11.py` | Video (`video/mp4` URI) | `noul` | Video input with `"low"` resolution setting: verifies presence of flames or fire (`shows_fire`). |
| `example12.py` | Text | `noul` | Common-sense reasoning validation: tests whether a car owner's plan to walk to drop off their car at a service center is valid. |
| `example13.py` | Text | `choice` | Formulates common-sense intention validation as a categorical choice (`yes` vs `no`) with descriptions. |
| `example14.py` | Text | `choice` | Action recommendation: determines whether the car owner should walk or drive to the service center. |

---

## Setup and Installation

### 1. Requirements
Install the Google GenAI SDK:
```bash
pip install google-genai
```

### 2. Configure API Key
Set your Gemini API key in your environment:
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Linux / macOS
export GEMINI_API_KEY="your-api-key-here"
```

### 3. Initialize the Client
The Decisions API is currently available in the `v1beta` API version:
```python
from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})
```

### 4. Running an Example
```bash
python example2.py
```

### 5. Formatting Responses as JSON
To print the complete response structure nicely formatted as indented JSON:
```python
# Using built-in SDK method
print(result.to_json())

# Or using Pydantic model dump
print(result.model_dump_json(indent=4))
```
