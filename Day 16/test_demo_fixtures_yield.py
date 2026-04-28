import pytest # pyright: ignore[reportMissingImports]

@pytest.fixture
def setup():
    print("Setup Browser")
    yield
    print("Close Browser")

def test_one(setup):
    print("This is my test one")

def test_two(setup):
    print("This is my test two")

def test_three(setup):
    print("This is my test three")