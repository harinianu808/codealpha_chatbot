import sys
def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm PyBot, your friendly neighborhood Python script."
    elif "weather" in user_input:
        return "I don't have a window, but it looks like 1s and 0s from here!"
    elif "python" in user_input:
        return "Python is my favorite language! It's elegant and powerful."
    elif "help" in user_input:
        return "I can answer questions about my name, the weather, or Python."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Could you try rephrasing?"
def start_chatbot():
    print("--- PyBot Rule-Based Chatbot ---")
    print("Type 'exit' or 'bye' to quit.")
    while True:
        user_message = input("\nYou: ")
        response = get_bot_response(user_message)
        print(f"PyBot: {response}")
        if "goodbye" in response.lower():
            break
if __name__ == "__main__":
    start_chatbot()