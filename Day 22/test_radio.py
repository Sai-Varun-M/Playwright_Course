from playwright.sync_api import Page, expect
import pytest # pyright: ignore[reportMissingImports]

@pytest.mark.skip(reason="This test is for demonstration purposes and may not be suitable for automated testing.")
def test_radio(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    male_radio = page.locator("label[for='male']")
    
    #To check visibility and enable state
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()


    #To see if checked or not
    expect(male_radio).not_to_be_checked()

    #Check radio button
    male_radio.check()

    #To see if checked
    expect(male_radio).to_be_checked()

    page.wait_for_timeout(5000)