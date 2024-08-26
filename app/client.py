import uuid

from langserve import RemoteRunnable

## Generate a new conversation_id or use a pre-existing
#  one if you're continuing a conversation
import base64



chat_service_url = "http://127.0.0.1:8000/web"

chat: RemoteRunnable = RemoteRunnable(chat_service_url)
r = chat.invoke({"web": "https://www.homecleaningservicemadrid.com/"})
print(r)

