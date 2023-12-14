import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()
API = genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

img = Image.open("studio.jpeg")
reponse = model.generate_content(["Write a blog post based on this picture. It should include how I can make this bathroom looks better",img])
print(reponse.text)
