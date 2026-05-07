import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect,Playwright # pyright: ignore[reportMissingImports]

#Browser-> context -> page
@pytest.mark.skip
def test_browser(playwright:Playwright):
    # chromium = playwright.chromium
    # browser = chromium.launch()

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)

    # expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    # expect(page2).to_have_title("Selenium")

