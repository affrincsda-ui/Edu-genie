
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

def summarize_text(text):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"""
            Summarize the following text for a
            college student.

            Use simple English.
            Include the main points as bullet points.
            Keep the summary short and clear.

            Text:
            {text}
            """
        )
        return response.text

    except Exception as e:
        return f"Error summarizing text: {e}"
      
