import logging
from langchain_core.prompts import BasePromptTemplate
from abc import ABC, abstractmethod


def load_prompt(filename):
    with open(filename, 'r') as file:
        return file.read()
    

class Prompt(ABC):
    """Use to handle basic AI prompt"""
    input_variables : list[str] = []
    text : str
    def __init__(self,file=None,text="",input_variables=""):
        logging.info("Initializing prompt object")
        if file == None:
            self.text = text
            self.input_variables = input_variables
        else:
            self.text = load_prompt(file)

    @abstractmethod
    def build() ->BasePromptTemplate:
        return


