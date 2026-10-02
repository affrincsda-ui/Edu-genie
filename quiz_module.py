
import os
import json
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv(
    "GEMINI_MODEL", "gemini-2.5-flash"
)

def generate_quiz(text):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"""
            Create exactly 3 multiple-choice questions
            based on this topic or passage:

            {text}

            Return only a valid JSON array.
            Each object must contain:
            question, options (4 strings),
            answer (correct option string).

            Example:
            [
              {{
                "question": "What is Python?",
                "options": [
                  "Language",
                  "Database",
                  "Browser",
                  "OS"
                ],
                "answer": "Language"
              }}
            ]
            """
        )

        result = response.text.strip()
        result = re.sub(
            r"^```(?:json)?\s*|\s*```$",
            "", result
        )

        return json.loads(result)

    except Exception as e:
        return {"error": str(e)}
      
