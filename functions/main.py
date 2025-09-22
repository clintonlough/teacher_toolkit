#Before running main, activate venv using -> source .venv/bin/activate

import os
import sys
import json
from system_prompt import get_base_prompt
from tools import get_tools

gpt_model="gpt-4o-mini"

# 1) Expose your function as a tool (Responses API style)
TOOLS, TOOLS_MAP = get_tools()

def print_cost(verbose, input_tokens,output_tokens, total_tokens, *, out=sys.stdout):
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

def run_with_tools(client, messages):
    resp = client.responses.create(
        model=gpt_model,
        input=messages,
        tools=TOOLS,
        parallel_tool_calls=False,
        tool_choice="auto",
    )

    while True:
        tool_calls = [item for item in resp.output if item.type == "function_call"]
        if not tool_calls:
            return resp  # final answer

        followups = []
        for call in tool_calls:
            args = json.loads(call.arguments or "{}")
            result = TOOLS_MAP[call.name](**args)          # list[dict] or similar
            if result is None:
                result = []                                # never send null

            followups.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": json.dumps(result, ensure_ascii=False),  # <-- stringify
            })

        resp = client.responses.create(
            model=gpt_model,
            input=followups,                  # send tool outputs
            previous_response_id=resp.id,     # keep state
            tools=TOOLS,                      # allow chaining if needed
            parallel_tool_calls=False,
            tool_choice="auto",
        )

def manage_conversation(verbose, messages, client):

    user_prompt = input("Prompt: ")
    if check_exit(user_prompt):
        return False

    messages.append({"role": "user", "content": user_prompt})

    # IMPORTANT: use the tool-enabled runner
    resp = run_with_tools(client, messages)

    print(resp.output_text)
    messages.append({"role": "assistant", "content": resp.output_text})
    print_cost(verbose, resp.usage.input_tokens, resp.usage.output_tokens, resp.usage.total_tokens)
    
    return True

def get_system_prompt():
    system_prompt = get_base_prompt()

    messages = [
    {"role": "developer", "content": system_prompt}
    ]

    return messages

def _get_client():
    from dotenv import load_dotenv  # local import, allows for unit tests without library dependencies
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set in environment or .env")
    from openai import OpenAI  # local import
    return OpenAI(api_key=api_key)


def main():

    verbose = check_verbose()
    client = _get_client()
    messages = get_system_prompt()
    #main conversation loop
    while True:
        keep_going = manage_conversation(verbose, messages, client)
        if keep_going is False:
            break



if __name__ == "__main__":
    main()