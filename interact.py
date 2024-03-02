import typing

import dotenv

from app.llm import chains


dotenv.load_dotenv('.env')


CHAIN_MAPPING = {
    "ripley_v1": chains.MISTRAL_RIPLEY_V1,
    "ripley_v2": chains.MISTRAL_RIPLEY_V2,
}


def prompt_user_for_chain() -> chains.SimpleLLMChain:
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


def interaction_loop(llm_chain: chains.SimpleLLMChain) -> None:
    while True:
        user_input = input(">>> ")

        if user_input in EXIT_STRINGS:
            break

        stream = llm_chain.chain.stream({"input": user_input})

        for message in stream:
            print(message, end="", flush=True)

        print('\n')


def main() -> None:
    chain = prompt_user_for_chain()
    interaction_loop(chain)


if __name__ == "__main__":
    main()