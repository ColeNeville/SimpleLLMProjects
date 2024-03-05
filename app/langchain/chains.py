import typing
import operator

import pydantic

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableLambda,
    RunnableSerializable,
)
from langchain_core.prompts import BaseChatPromptTemplate, PromptTemplate
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.memory import (
    ChatMessageHistory,
    ConversationBufferMemory, 
    ConversationEntityMemory,
)

from langchain.memory.chat_memory import BaseChatMemory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage

from app.langchain import prompts, chat_models


class ChainManager():
    language_model: BaseChatModel
    prompt: PromptTemplate
    memory: typing.Optional[BaseChatMemory]


    def __init__(
        self,
        language_model: BaseChatModel,
        prompt: PromptTemplate,
        memory: typing.Optional[BaseChatMemory] = None,
    ) -> None:
        self.language_model = language_model
        self.prompt = prompt
        self.memory = memory


    def get_memory_messages(
        self,
        inputs: typing.Dict[str, typing.Any],
    ) -> typing.Dict[str, typing.Any]:
        if self.memory is None:
            return []

        return self.memory.load_memory_variables(inputs) | inputs


    def build_chain(self) -> RunnableSerializable[typing.Dict, typing.Any]:
        return (
            RunnableLambda(self.get_memory_messages)
            | self.prompt
            | self.language_model
            | StrOutputParser()
        )


    def add_interaction_to_memory(
        self,
        user_input: str,
        ai_response: str
    ) -> None:
        if self.memory is not None:
            self.memory.save_context({"user": user_input}, {"ai": ai_response})


RIPLEY_CONVERSATION_CHAIN_MANAGER = ChainManager(
    language_model=chat_models.MISTRAL,
    prompt=prompts.RIPLEY_CONVERSATION,
    memory=ConversationBufferMemory(),
)

RIPLEY_ENTITY_CONVERSATION_CHAIN_MANAGER = ChainManager(
    language_model=chat_models.MISTRAL,
    prompt=prompts.RIPLEY_ENTITY_CONVERSATION,
    memory=ConversationEntityMemory(
        llm=chat_models.MISTRAL
    ),
)
