import openai
import os
from dotenv import load_dotenv

from prompts.expanding_text import prompt


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.0):
    messages = [{
        "role": "user",
        "content": prompt,
    }]
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message["content"]


if __name__ == "__main__":        
    response = get_completion(prompt, temperature=0.5)
    print(response)
