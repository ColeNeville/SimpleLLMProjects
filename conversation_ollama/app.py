from operator import itemgetter
from dotenv import load_dotenv

from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import (
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  MessagesPlaceholder,
  StringPromptTemplate,
  PromptTemplate,
)
from langchain_core.messages import (
  SystemMessage,
  HumanMessage,
)
from langchain_core.runnables import (
  RunnablePassthrough,
  RunnableLambda,
)
from langchain.memory import ConversationBufferMemory

load_dotenv(dotenv_path="../.env")

memory = ConversationBufferMemory(return_messages=True)

prompt = ChatPromptTemplate.from_messages([
  SystemMessage(content="You are a friendly virtual assisant."),
  MessagesPlaceholder(variable_name="history"),
  HumanMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["input"], template="{input}"),
  )
])

print(prompt)

# model = Ollama(model="neural-chat")

# chain = (
#   RunnablePassthrough.assign(
#     history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
#   )
#   | prompt
#   | model
# )

# user_input = ''

# while True:
#   user_input = input(">>")

#   if user_input == '/exit':
#     break

#   # print("current user input: ", user_input)
#   # print("current memory: ", memory.load_memory_variables({"input": user_input}))
#   # print("current prompt: ", prompt.invoke({"input": user_input, "history": memory.load_memory_variables({"input": user_input})}))

#   stream = chain.stream({"input": user_input})

#   output = ''

#   for message in stream:
#     print(message, end='', flush=True)
#     output = output + message.join('')


#   memory.save_context({"input": user_input}, {"output": output})
    
#   print('\n')
