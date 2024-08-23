import uuid

from langserve import RemoteRunnable

## Generate a new conversation_id or use a pre-existing
#  one if you're continuing a conversation
import base64

with open("/home/developer/Documents/credits/Experian.pdf", "rb") as f:
    data = f.read()

encoded_data = base64.b64encode(data).decode("utf-8")
chat_service_url = "http://127.0.0.1:8000/pdf"

chat: RemoteRunnable = RemoteRunnable(chat_service_url)
r = chat.invoke({"file": encoded_data})
print(r)

