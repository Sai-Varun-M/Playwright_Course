import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import expect, Page, Playwright # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_authpop(playwright:Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://admin:admin@the-internet.herokupp.com/basic_auth")
    page.wait_for_load_state()

    expect(page.locator("text=Congratulation")).to_be_visible()
    page.wait_for_timeout(3000)

@pytest.mark.skip
def test_authpop_context(playwright:Playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context(http_credentials = {"username":"admin","password":"admin"})
    page = context.new_page()

    page.goto("https://admin:admin@the-internet.herokupp.com/basic_auth")
    page.wait_for_load_state()

    expect(page.locator("text=Congratulation")).to_be_visible()
    page.wait_for_timeout(3000)