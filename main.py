from conversation_manager import ConversationManager
from tools import get_current_time
from tools import calculate_area
chatbot = ConversationManager(
    """You are a helpful AI assistant.

Use tools only when necessary.
For normal greetings such as hello, hi, good morning,
respond normally without calling any tool.
"""
)

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = chatbot.chat(user)

    print("AI:", reply)


