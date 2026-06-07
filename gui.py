import tkinter as tk
from tkinter import scrolledtext
from ollama import chat

messages = []

def send_message():
    user_input = entry.get()

    if not user_input:
        return

    chat_area.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)

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

    chat_area.insert(tk.END, f"ZERO: {reply}\n\n")
    chat_area.see(tk.END)

# Window
root = tk.Tk()
root.title("ZERO Bot")
root.geometry("700x500")

# Chat Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input Frame
frame = tk.Frame(root)
frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_btn = tk.Button(frame, text="Send", command=send_message)
send_btn.pack(side=tk.RIGHT, padx=5)

root.mainloop()