from ollama import chat
import json


MODEL = "llama3.2:3b"


LEARNING_PROMPT = """
Classify the user's message into exactly ONE category.

ANSWER = simple factual answer
EXPLAIN = explain a concept
TEACH = user needs guided teaching
PRACTICE = user asks for practice
EVALUATE = user wants an answer checked

Examples:

"What is the capital of India?" -> ANSWER
"What is Python?" -> EXPLAIN
"Explain functions in Python." -> EXPLAIN
"I don't understand derivatives." -> TEACH
"Teach me Python." -> TEACH
"Give me a Python problem." -> PRACTICE
"I got x = 5. Is that correct?" -> EVALUATE

Return ONLY one word:
ANSWER
EXPLAIN
TEACH
PRACTICE
EVALUATE
"""


def decide_action(question):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": LEARNING_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    content = response.message.content.strip()

    try:

        result = json.loads(content)

        action = result.get("action")

        allowed_actions = {
            "ANSWER",
            "EXPLAIN",
            "TEACH",
            "PRACTICE",
            "EVALUATE"
        }

        if action in allowed_actions:
            return action

    except json.JSONDecodeError:
        pass

    return "ANSWER"


if __name__ == "__main__":

    questions = [
        "What is the capital of India?",
        "What is Python?",
        "Explain functions in Python",
        "I don't understand derivatives",
        "Give me a Python problem",
        "I got x = 5. Is that correct?"
    ]

    for question in questions:

        action = decide_action(question)

        print(question)
        print("Action:", action)
        print()