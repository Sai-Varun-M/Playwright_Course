import pytest # pyright: ignore[reportMissingImports]

@pytest.mark.order(1)
def test_login():
    print("This is login test")

@pytest.mark.order(3)
def test_add_item():
    print("This is add item test")

@pytest.mark.order(2)
def test_logout():
    print("This is logout")