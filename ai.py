import openai
import os
openai.api_key = 

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
       prompt_response = response_dict[0]["text"]
    return prompt_response
