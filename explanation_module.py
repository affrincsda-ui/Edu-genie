
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv(
    "GEMINI_MODEL", "gemini-2.5-flash"
)

def explain_topic(topic):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"""
            Explain the topic '{topic}' in very
            simple language for a college student.

            Include:
            1. Definition
            2. Main points
            3. Simple example
            4. Short conclusion
            """
        )
        return response.text

    except Exception as e:
        return f"Error explaining topic: {e}"
      
