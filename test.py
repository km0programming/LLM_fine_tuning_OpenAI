import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# print(OPENAI_API_KEY)

import openai

# print(openai.__version__)


from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
#   model="gpt-4o-mini-2024-07-18",
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    # {"role": "user", "content": "Please list the most important newspapers in Spain?"}
    {"role": "user", "content": "Tell me something about Mercedes-Benz'?"}
  ]
)

print(completion.choices[0].message.content)




