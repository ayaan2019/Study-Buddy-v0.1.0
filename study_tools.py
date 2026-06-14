from typing import List

def create_quiz(topic: str) -> List[str]:
    return [
        f"What is {topic}?",
        f"Why is {topic} important?",
        f"Give one example of {topic}.",
    ]

def create_flashcards(topic: str) -> List[str]:
    return [
        f"{topic} - Definition",
        f"{topic} - Example",
        f"{topic} - Key Facts",
    ]