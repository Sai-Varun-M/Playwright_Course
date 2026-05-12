from playwright.sync_api import Playwright, expect, Page

def test_showdow(page:Page):
    page.goto("https://books-pwakit.appspot.com/")
    page.get_by_role('textbox',name = 'Search Books').fill("welcome")
    page.wait_for_timeout(3000)
    