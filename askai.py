import os
from mistralai import Mistral
from dotenv import load_dotenv
from pecan import response
from voluptuous import message

from main import question

load_dotenv()
api_key=os.getenv('API_KEY')
client = Mistral(api_key=api_key)
model = 'mistral-small-latest'
question = 'What is the secret of the universe?'
messages = [
    {'role': 'user', 'content': question}
]
response = client.chat.complete(
    model=model,
    messages=messages,
    max_tokens=300,
    temperature=0.7
)
print(response.choices[0].message.content)