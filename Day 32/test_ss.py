from playwright.sync_api import Page,expect # pyright: ignore[reportMissingImports]
import time
import datetime

def test_ss(page:Page):
    page.goto("https://www.demoblaze.com/index.html")

    timestamp = str(int(time.time()))

    page.screenshot(path=f"screenshots/homepage_{timestamp}.png") #Partially Visible

    page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page = True) #Full Page

    logo = page.locator("a[id='nava'] img")
    logo.screenshot(path=f"screenshots/homepage_{timestamp}.png") #Specific element screenshot
    