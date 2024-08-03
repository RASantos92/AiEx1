from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("myGptkey"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "write a haiku about ai"}
    ]
)


print(type(completion), "\n", completion.model,"\n", completion, "\n",completion.choices[0].message.content )

completion_data = {
    "model": completion.model,
}

# Write the completion information to a JSON file
with open("completion_data.json", "w") as json_file:
    json.dump(completion_data, json_file, indent=4)

# Print confirmation
print("Completion data saved to completion_data.json")