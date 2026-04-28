import pytest # pyright: ignore[reportMissingImports]

@pytest.fixture
def setup():
    print("Setup Browser")
    return "Chrome"

def test_one(setup):
    print("This is my test one")
    print("Browser is:",setup)

def test_two(setup):
    print("This is my test two")
    print("Browser is:",setup)

def test_three(setup):
    print("This is my test three")
    print("Browser is:",setup)