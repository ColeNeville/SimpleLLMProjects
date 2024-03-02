from langchain_community.llms.ollama import Ollama
from langchain_openai import OpenAI


NEURAL_CHAT = Ollama(model="neural-chat")
MISTRAL = Ollama(model="mistral")

GPT3 = OpenAI(model="gpt-3.5-turbo")
GPT4 = OpenAI(model="gpt-4-turbo")
