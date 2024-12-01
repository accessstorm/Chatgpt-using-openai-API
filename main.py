import openai

# Replace with your actual OpenAI API key
openai.api_key = '#'

def chat_with_gt(prompt):
    # Using the new API
    response = openai.completions.create(
        model="gpt-3.5-turbo", 
        prompt=prompt,
        max_tokens=1
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("Chatbot: Goodbye!")
            break

        try:
            response = chat_with_gt(user_input)
            print("Chatbot:", response)
        except Exception as e:
            print("An error occurred:", str(e))
