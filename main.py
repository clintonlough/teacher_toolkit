from openai import OpenAI
import os
import sys

#accesses the stored API key from .env
from dotenv import load_dotenv
load_dotenv()


# Create a client with your key from the environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
gpt_model="gpt-4o-mini"

def print_cost(verbose, input_tokens,output_tokens, total_tokens):
    if verbose == True:
        # USD per 1 million tokens
        input_cost = 0.15 / 1_000_000
        output_cost = 0.60 / 1_000_000

        print("Input tokens:", input_tokens)
        print("Output tokens:", output_tokens)
        print("Total tokens:", total_tokens)

        total_cost = (input_tokens * input_cost) + (output_tokens * output_cost)
        print(f"Estimated cost is USD ${total_cost:.5f}")

def check_verbose():
    for arg in sys.argv[1:]:
        if arg == "--verbose":
            return True
    return False

def check_exit(user_prompt):
    if user_prompt == "quit":
        return True

def manage_conversation(verbose, messages):

    user_prompt = input("Prompt: ")

    if check_exit(user_prompt):
        return False
    
    messages.append({"role": "user", "content": user_prompt})
    
    
    resp = client.responses.create(model=gpt_model, input=messages)

    print(resp.output_text)
    messages.append({"role": "assistant", "content": resp.output_text})
    
    print_cost(verbose, resp.usage.input_tokens,resp.usage.output_tokens, resp.usage.total_tokens)

def get_system_prompt():
    system_prompt = "You are a trivia master. Always respond with a trivia fact and limit your response to 20 words or less."

    messages = [
    {"role": "developer", "content": system_prompt}
    ]

    return messages

def main():

    verbose = check_verbose()
    messages = get_system_prompt()
    #main conversation loop
    while True:
        manage_conversation(verbose, messages)
        


if __name__ == "__main__":
    main()