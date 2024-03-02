import typing
import operator

from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableLambda,
    RunnableSerializable,
)

from langchain.memory import ConversationBufferMemory, PostgresChatMessageHistory

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
)

from langchain_core.messages import BaseMessage
from langchain.llms.base import BaseLLM
from langchain_core.memory import BaseMemory

from app.llm import (
    models, templates, memories
)


class SimpleLLMChain():
    chain: RunnableSerializable[typing.Dict, typing.Any]
    memory: BaseMemory | None = None


    def __init__(
        self,
        chain: RunnableSerializable[typing.Dict, typing.Any],
    ) -> None:
        self.chain = chain


    def add_to_memory(self) -> None:
        pass


    @classmethod
    def build(
        cls: type[typing.Self],
        prompt_template: PromptTemplate | ChatPromptTemplate,
        model: BaseLLM,
        memory: BaseMemory | None = None,
    ) -> typing.Self:
        chain: RunnableSerializable[typing.Dict, typing.Any] = (prompt_template | model)

        if memory is not None:
            chain = (
                RunnablePassthrough.assign(
                    history=(
                        RunnableLambda(memory.load_memory_variables)
                        | operator.itemgetter('history')
                    )
                )
            ) | chain

        return cls(chain=chain)


MISTRAL_RIPLEY_V1 = SimpleLLMChain.build(
    prompt_template=templates.RIPLEY_V1,
    model=models.MISTRAL,
)

MISTRAL_RIPLEY_V2 = SimpleLLMChain.build(
    prompt_template=templates.RIPLEY_V2,
    model=models.MISTRAL,
    memory=ConversationBufferMemory(return_messages=True),
)