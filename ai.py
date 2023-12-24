import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyC3pLN_QqQYVRYA4lgxhgk0Oi4VPAHsISo"
genai.configure(api_key=GOOGLE_API_KEY)

basic_prompt = ", act as if your name is racoon and you are very funny, your a chat bot so talk in one sentence, dont say anything bad"

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])
def generate_response(question):
    try:
        response = chat.send_message(question + basic_prompt)
    except:
        return "looks like we may be having content that violates my protocols, so try again"
    return response.text

