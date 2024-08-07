import uuid
from langserve import RemoteRunnable
import os

# Generate a new conversation_id or use a pre-existing one if you're continuing a conversation
conversation_id = str(uuid.uuid4())

chat_service_url = "http://127.0.0.1:8000/"
user_id = "sample_user" 

chat = RemoteRunnable(chat_service_url, cookies={"user_id": user_id})

q = input("User (q to quit): ")
while q!="q":
    response = chat.invoke(
        {"human_input":q},
            {
                "configurable": {
                    "conversation_id": conversation_id,
            },
        },
    )
    print(f"AI: {response.content}")
    q = input("User (q to quit): ")

