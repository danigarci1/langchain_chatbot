from app import get_chain


def test_my_chain() -> None:
    chain = get_chain()
    chain.invoke({"human_input": "foo","history":[]})
