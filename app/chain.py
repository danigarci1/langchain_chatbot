from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableSerializable
from app.prompt.chat import ChatPrompt

def get_chain() -> RunnableSerializable:
    promptTemplate = ChatPrompt('chatbot.prompt')

    chain = promptTemplate.build() | ChatOpenAI()
    return chain
