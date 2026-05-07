import pytest  # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_mouse(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pointme = page.locator(".dropbtn")
    pointme.hover()

    laptops = page.locator('.dropdown-content a:nth-child(2)')
    laptops.hover()

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_mouse_doubleclick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    btncopy = page.locator("button[ondblclick='myFunction1()']")
    btncopy.dblclick() #performs double click action
    field2 = page.locator('#field2')
    expect(field2).to_have_value("Hello World!")

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_draganddrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source = page.locator("#draggable")
    target = page.locator("#droppable")

    #Approach 1
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    #Approach 2
    source.drag_to(target)

    page.wait_for_timeout(5000)