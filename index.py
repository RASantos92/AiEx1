from openai import OpenAI
import json
from dotenv import load_dotenv
import os
from datetime import date

load_dotenv()

client = OpenAI(api_key=os.getenv("myGptkey"))

user_prompt = input("Please enter your prompt for the AI: ")


def makeAPICall(text):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "Your a helpful tutor that uses a mix of two methods, that include the socratic and Elenchus methods. These methods are known for their thought-provoking and dialogue-based approach learning, it encourages learners to ask questions, explore ideas, and uncover their own answers. make sure to return the response to JSON."},
            {"role": "user", "content": text}
        ]
    )
    
    
    completion_data = {
    "model": completion.model,
    "message": completion.choices[0].message.content
}
    # Write the completion information to a JSON file
    with open("completion_data.json", "w") as json_file:
        json.dump(completion_data, json_file, indent=4)

    # Print confirmation
    print("Completion data saved to completion_data.json")
    return completion.choices[0].message.content



print("before the function")

def talk():
    messages = [
    ]
    messages.append({"role": "system", "content": "You are a Teacher specializing in math. You will not give straight answers and instead promote critical thinking"})
    print("before the while")
    while True:
        print("before the try")
        try:
            print("we got here")
            prompt = input()
            print(makeAPICall(prompt))
        except KeyboardInterrupt:
            break


talk()