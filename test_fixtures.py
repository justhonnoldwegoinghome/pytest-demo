import pytest


@pytest.fixture
def my_pet():
    print("Fixture setup")
    yield "dog"
    print("Fixture teardown")


def test_pet(my_pet):
    print("Test", my_pet)
    assert my_pet == "dog"
