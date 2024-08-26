from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSerializable

def load_prompt(filename):
    with open(filename, 'r') as file:
        return file.read()

prompt = load_prompt('.prompt')


def get_chain() -> RunnableSerializable:
    promptTemplate = PromptTemplate(
    input_variables=["text"],
    template=prompt,
    )
    chain = promptTemplate | ChatOpenAI()
    return chain
