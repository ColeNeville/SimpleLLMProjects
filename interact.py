import typing
import dotenv

from app.langchain import chains


dotenv.load_dotenv('.env')


CHAIN_MAPPING: typing.Dict[typing.LiteralString, chains.ChainManager] = {
    "ripley": chains.RIPLEY_CONVERSATION_CHAIN_MANAGER,
    "ripley_entity": chains.RIPLEY_ENTITY_CONVERSATION_CHAIN_MANAGER,
}


def prompt_user_for_chain() -> chains.ChainManager:
    while True:
        chain_name = input("Please enter the name of the chain you would like to use: ")

        if chain_name not in CHAIN_MAPPING:
            print("Chain not found")
            print("Valid chains are:")

            for chain in CHAIN_MAPPING:
                print(chain)
        else:
            return CHAIN_MAPPING[chain_name]


EXIT_STRINGS = ['exit', '/exit']


def interaction_loop(
    chain_manager: chains.ChainManager
) -> None:
    while True:
        user_input = input(">>> ")

        if user_input in EXIT_STRINGS:
            break

        stream = chain_manager.build_chain().stream({"input": user_input})

        whole_response = ''

        for message in stream:
            whole_response += message
            print(message, end="", flush=True)

        chain_manager.add_interaction_to_memory(user_input, whole_response)

        print('\n')


def main() -> None:
    chain_manager = prompt_user_for_chain()
    interaction_loop(chain_manager)


if __name__ == "__main__":
    main()