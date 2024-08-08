from langchain.chat_models.openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableSerializable


def get_chain() -> RunnableSerializable:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You're an assistant by the name of Bob."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{human_input}"),
        ]
    )

    chain = prompt | ChatOpenAI()
    return chain
