
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

def get_learning_recommendations(topic):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"""
            You are EduGenie, a learning assistant.

            Create a simple learning path for
            a college student who wants to learn:
            {topic}

            Include:
            1. Beginner topics
            2. Intermediate topics
            3. Advanced topics
            4. Practice activities
            5. Final project idea

            Explain in simple English.
            Use headings and bullet points.
            """
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"
      
