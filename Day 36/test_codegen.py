import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoblaze.com/index.html")
    page.get_by_role("link", name="PRODUCT STORE").click()
    expect(page.get_by_role("link", name="PRODUCT STORE")).to_be_visible()
    expect(page.get_by_role("link", name="Log in")).to_be_visible()
    expect(page.get_by_role("link", name="About us")).to_be_visible()
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").click()
    page.locator("#loginusername").click()
    page.locator("#loginpassword").click()
    page.locator("#loginpassword").click()
    page.get_by_label("Log in").get_by_text("Close").click()
