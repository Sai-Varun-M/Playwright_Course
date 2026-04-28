#scope="function" : fixture will be called before every test function executes
#scope="module" : fixture will be called only once before test funcions executes
#scope="class" : fixture will be called only once before the class
#scope="session" : fixture will be called only once for session
#moduel-> class-> methods
#module-> function

import pytest # pyright: ignore[reportMissingImports]

@pytest.fixture
def setup(scope="module"):
    print("Setup Browser")

def test_one(setup):
    print("This is my test one")

def test_two(setup):
    print("This is my test two")

def test_three(setup):
    print("This is my test three")