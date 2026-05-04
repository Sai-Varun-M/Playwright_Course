from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_keyboard(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1 = page.locator("#input1")
    input1.focus()

    page.keyboard.insert_text("welcome")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    input2=page.locator("#input2")
    input3=page.locator("#input3")

    expect(input2).to_have_value("welcome")
    expect(input3).to_have_value("welcome")

    page.wait_for_timeout(3000)