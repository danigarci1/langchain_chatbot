from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableSerializable

def load_prompt(filename):
    with open(filename, 'r') as file:
        return file.read()

prompt = load_prompt('.prompt')

def get_chain() -> RunnableSerializable:
    promptTemplate = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{human_input}"),
        ]
    )

    chain = promptTemplate | ChatOpenAI()
    return chain
