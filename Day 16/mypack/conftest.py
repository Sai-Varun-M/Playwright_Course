import pytest # pyright: ignore[reportMissingImports]

@pytest.fixture
def setup():
    print("Setup Environment")
    yield
    print("Setup Close")