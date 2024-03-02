import os

from langchain_openai import ChatOpenAI
from langchain.prompts import (
  ChatPromptTemplate,
  MessagesPlaceholder
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
prompt = ChatPromptTemplate(message=[
  ("system", "You are Ripley a fantastic virtual assistant and friendy conversationalist always striving to keep the conversation going."),
  MessagesPlaceholder(variable_name="chat_history")
  ("user", "{input}")
])
memory = ConversationBufferMemory(memory_key="chat_history")
language_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

conversaton = LLMChain(
  prompt=prompt,
  memory=memory,
  verbose=True,
  llm=language_model,
)

user_input = ''


while True:
  user_input = input(">>")

  if user_input == '/exit':
    break

  print(conversaton({"input": user_input}))