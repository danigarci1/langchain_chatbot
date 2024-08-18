from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableSerializable
from app.prompts import assistant_basic_prompt

def get_chain() -> RunnableSerializable:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", assistant_basic_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{human_input}"),
        ]
    )

    chain = prompt | ChatOpenAI()
    return chain
