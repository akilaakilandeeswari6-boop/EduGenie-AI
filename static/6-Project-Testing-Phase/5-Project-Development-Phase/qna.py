import google.generativeai as genai

# NOTE: Make sure you configure your API key somewhere in your project!
# genai.configure(api_key="YOUR_API_KEY_HERE")

def answer_question_with_gemini(question: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="gemini-3.6-flash")
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"