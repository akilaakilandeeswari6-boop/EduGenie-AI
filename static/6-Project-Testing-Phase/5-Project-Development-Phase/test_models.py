from explanation_module import get_explanation
from qna import get_answer

print("Testing Local Model (LaMini)...")
print(get_explanation("Explain gravity briefly."))

print("\nTesting Cloud Model (Gemini)...")
print(get_answer("Say hello in one word."))