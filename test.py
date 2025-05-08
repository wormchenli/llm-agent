# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")  # Load variables from .env file

api_key = config.get("API_KEY")
base_url = config.get("BASE_URL")

client = OpenAI(api_key=api_key, base_url=base_url)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)
print(response.choices[0].message.content)
