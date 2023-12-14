import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API = genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

while True:
    prompt = input("Write your inquiry: ")
    response = chat.send_message(prompt)
    print(response.text)
    if prompt == "break":
        break



print(chat.history)