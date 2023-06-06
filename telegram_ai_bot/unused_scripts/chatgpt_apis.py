import openai
from dotenv import load_dotenv
from telegram_ai_bot.config.settings import OPENAI_API_KEY

load_dotenv('../.env')

openai.api_key = OPENAI_API_KEY
# models = openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(f'{type(completion.choices)} :: {completion.choices[0].message}')
