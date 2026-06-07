from ollama import chat

messages = []

print("ZERO Bot Started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("ZERO: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = chat(
        model="qwen2.5:1.5b",
        messages=messages
    )

    reply = response["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": reply
    })

    print("ZERO:", reply)
    

    