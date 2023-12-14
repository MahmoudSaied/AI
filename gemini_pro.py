import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
API = genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


prompt = input("Write your inquiry: ")
response = model.generate_content(prompt)

for chunk in response:
    print(chunk.text)
    print("_"*80)