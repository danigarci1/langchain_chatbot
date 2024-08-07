from app import get_chain


def test_my_chain() -> None:
    """Edit this test to test your chain."""
    chain = get_chain()
    chain.invoke({"human_input": "foo"})
