from openai import OpenAI
from config import apikey

client = OpenAI(api_key=apikey)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Write an email to my boss for resignation"
        }
    ]
)

print(response.choices[0].message.content)