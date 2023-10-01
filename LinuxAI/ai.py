#Chat GPT for Linux Ubuntu 20.04 

import requests
#!!!!!!!!!!!!!!!!
OPENAI_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenAI API Key!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!
def generate_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    data = {
        "prompt": prompt,
        "max_tokens": 50,  #Adjust as needed
        
    }

    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions", 
        headers=headers, 
        json=data
    )

    return response.json().get('choices')[0].get('text')

if __name__ == "__main__":
    prompt = input("Enter a prompt: ")
    result = generate_ai_response(prompt)
    print(result)
