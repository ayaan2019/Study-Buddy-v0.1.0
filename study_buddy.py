from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are StudyBuddy.

You help students:
- Understand concepts
- Answer questions
- Create quizzes
- Create flashcards

Keep explanations simple and beginner friendly.
"""

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nStudent: {question}"
    )

    print("\nStudyBuddy:", response.text)