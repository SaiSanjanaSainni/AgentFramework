from llm_client import client
from tool_schema import TOOLS
import json
from tools import get_current_time, calculate_area, read_file
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
            messages=self.messages,
            tools=TOOLS
        )
        reply=response.choices[0].message
        if reply.tool_calls:
            tool_name=reply.tool_calls[0].function.name
            if tool_name=="get_current_time":
                result=get_current_time()
                self.messages.append(
                    {
                        "role": "assistant",
                        "content": result
                    }
                )
                return result
            if tool_name=="calculate_area":
                arguments=json.loads(reply.tool_calls[0].function.arguments)
                length=arguments["length"]
                width=arguments["width"]
                result=calculate_area(length,width)
                self.messages.append(
                    {
                        "role": "assistant",
                        "content": str(result)
                    }
                )
                return result
            if tool_name=="read_file":
                arguments=json.loads(reply.tool_calls[0].function.arguments)
                filename=arguments["filename"]
                result=read_file(filename)
                self.messages.append(
                    {
                        "role":"assistant",
                        "content": result
                    }
                )
                return result

        r=reply.content
        self.messages.append(
            {
                "role":"assistant",
                "content":r
            }
        )
        return r
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
