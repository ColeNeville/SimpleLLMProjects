from langchain_community.chat_models import ChatOllama
from langchain_community.llms.ollama import Ollama


MISTRAL = ChatOllama(model="mistral", base_url="http://goblin.local.coleslab.com:11434")
NEURAL_CHAT = ChatOllama(model="neural-chat", base_url="http://goblin.local.coleslab.com:11434")
