import re
import json
from groq import Groq
import os

def extract_summary_from_ocr(text):
    prompt = f"""
You are an information extractor.

Given the OCR bill text, extract:
- name
- email
- total_amount

Return in this format:
{{
  "name": "...",
  "email": "...",
  "total_amount": "..."
}}
Note, total amount should be a plain number without symbols
if any value is missing, let the value be null.
Following is the text you need to extract :

Text:
\"\"\"{text}\"\"\"
"""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an extractor."},
            {"role": "user", "content": prompt}
        ]
    )
    raw = response.choices[0].message.content
    json_match = re.search(r'\{.*?\}', raw, re.DOTALL)
    return json.loads(json_match.group()) if json_match else {}


import os
import re
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def extract_user_payments(ocr_text):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are an information extractor.

Given the OCR-extracted bill text below, extract all user entries where each entry includes:
- name
- email
- amount_paid (not total bill amount, but individual user-paid amount)

Return an array of JSON objects like this:
[
  {{
    "name": "...",
    "email": "...",
    "amount_paid": "..."
  }},
  ...
]

Only return valid entries. If a field is missing, return null.
Here is the OCR text:
\"\"\"{ocr_text}\"\"\"
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an information extractor that strictly follows the JSON format."},
            {"role": "user", "content": prompt}
        ]
    )

    llm_raw_output = response.choices[0].message.content.strip()
    json_array_match = re.search(r'\[\s*{.*?}\s*]', llm_raw_output, re.DOTALL)

    if json_array_match:
        try:
            return json.loads(json_array_match.group())
        except Exception as e:
            print("❌ Failed to parse JSON:", e)
            return []
    else:
        print("❌ No valid JSON found.")
        print("🔎 Raw response:", llm_raw_output)
        return []
