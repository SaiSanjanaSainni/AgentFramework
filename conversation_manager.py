from llm_client import client
class ConversationManager:
    def __init__(self,system_prompt):
        self.system_prompt=system_prompt
        self.messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ]
    def add_user_message(self,text):
        self.messages.append(
            {
                "role": "user",
                "content": text
            }
        )
    def get_response(self):
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.messages
        )
        reply=response.choices[0].message.content
        self.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )
        return reply
    def chat(self,text):
        self.add_user_message(text)
        return self.get_response()
    def get_history(self):
        return self.messages
    def clear(self):
        self.messages=[
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]