from app.prompt.base import Prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import logging

class ChatPrompt(Prompt):

    def build(self):
        if len(self.input_variables)==0:
            logging.warning("Not valid input variables. Setting user input to 'human_input'")
            self.input_variables = ["human_input"]
        promptTemplate = ChatPromptTemplate.from_messages(
        [
            ("system", self.text),
            MessagesPlaceholder(variable_name="history"),
            ("human", self.input_variables[0]),
        ]
        )
        return promptTemplate