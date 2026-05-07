import pytest
from playwright.sync_api import Page, expect, Playwright # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_popups(playwright:Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    # def handle_popup(popup):
    #     popup.wait_for_load_state()

    # page.on("popup",handle_popup)

    page.on("popup", lambda popup:popup.wait_for_load_state())

    page.locator("#PopUp").click()

    page.wait_for_timeout(3000)

    all_popups = context.pages
    print("Total Number Of Popups:-",len(all_popups))
    
    #Url of all pages
    for pw in all_popups:
        print(pw.url)
        title = pw.title()
        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(3000)
            expect(pw).to_have_title("Installation | Playwright")
            pw.close() # Close the playwright Popups

    page.wait_for_timeout(3000)
    context.close()
    browser.close()