from langchain_core.prompts import (
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  PromptTemplate,
  MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage

from app.llm import personalities


BASIC_PROMPT_TEMPLATE = PromptTemplate(input_variables=["input"], template="{input}")


RIPLEY_V1 = ChatPromptTemplate.from_messages([
  SystemMessage(content=personalities.RIPLEY_V1),
  HumanMessagePromptTemplate(prompt=BASIC_PROMPT_TEMPLATE),
])

RIPLEY_V2 = ChatPromptTemplate.from_messages([
    SystemMessage(content=personalities.RIPLEY_V1),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate(prompt=BASIC_PROMPT_TEMPLATE),
])
