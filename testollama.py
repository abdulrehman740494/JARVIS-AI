import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': 'Who are you?'
        }
    ]
)

print(response['message']['content'])