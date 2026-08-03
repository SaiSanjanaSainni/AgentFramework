from conversation_manager import ConversationManager

chatbot = ConversationManager(
    "You are a helpful AI assistant."
)

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = chatbot.chat(user)

    print("AI:", reply)