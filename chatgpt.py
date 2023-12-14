from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

prompt = "Recommend me few projects that I can do in python"

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)