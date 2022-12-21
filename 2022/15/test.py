import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  temperature=0.7,
  max_tokens=1010,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
openai.Engine.retrieve("text-davinci-003")
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)
t=1