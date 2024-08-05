from openai import OpenAI
import json
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()

client = OpenAI(api_key=os.getenv("myGptkey"))

def makeAPICall(contextBox):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= contextBox
    )

    # Print confirmation
    print("Completion data saved to completion_data.json")
    return completion.choices[0].message.content

print("before the function")

def talk():
    messages = []
    messages.append({"role": "system", "content": "Your a helpful math tutor that uses thought-provoking and dialogue-based approach learning. Make sure to answer in a question format."})
    print("before the while")
    while True:
        print("before the try")
        try:
            print("we got here")
            prompt = input()
            messages.append({"role":"user", "content": prompt})
            response = makeAPICall(messages)
            messages.append({'role': 'system', 'content': response})
        except KeyboardInterrupt:
            break


talk()