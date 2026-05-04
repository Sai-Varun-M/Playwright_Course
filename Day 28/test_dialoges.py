import pytest  # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_dialoges(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)
    
    def handle_dialog(dialog): #Registering an event
        dialog.accept()
    
    page.on("dialog",handle_dialog) 
    page.wait_for_timeout(3000)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(3000)
    
@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(3000)

    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_confirm_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(3000)

    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)

    text= page.locator("#demo").inner_text()
    print("Output Text:",text)

    expect(page.locator('#demo')).to_have_text("You pressed OK!")
    page.wait_for_timeout(3000)

def test_prompt_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog",lambda dialog:dialog.accept('John'))
    page.locator("#promptBtn").click()
    text = page.locator("#demo").inner_text()
    print("Output text:",text)
    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")