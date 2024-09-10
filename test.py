import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

print(OPENAI_API_KEY)

import openai



# print(openai.__version__)


  # Define the system prompt
system_prompt = "Given the medical description report, classify it into one of these categories: " + \
              "[Cardiovascular / Pulmonary, Gastroenterology, Neurology, Radiology, Surgery]"

from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# completion = client.chat.completions.create(
# #   model="gpt-4o-mini-2024-07-18",
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     # {"role": "user", "content": "Please list the most important newspapers in Spain?"}
#     {"role": "user", "content": "Tell me something about Mercedes-Benz'?"}
#   ]
# )



completion = client.chat.completions.create(
#   model="gpt-4o-mini-2024-07-18",
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_prompt},
    # {"role": "user", "content": "Please list the most important newspapers in Spain?"}
    {"role": "user", "content": "Tell me something about Mercedes-Benz'?"}
  ]
)

print(completion.choices[0].message.content)




