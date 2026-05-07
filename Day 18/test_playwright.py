#Use  pytest test_playwright.py -s -v --headed  to see UI
# To run to two or more browsers:-  pytest test_playwright.py -s -v --headed --browser webkit --browser chromium         

from playwright.sync_api import Page,expect # pyright: ignore[reportMissingImports]

def test_verifyPageUrl(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/") #Passing Url
    myurl=page.url
    print("Url Of the Application:",myurl)
    # expect(page).to_have_url("https://testautomationpractice.blogspot.com/") #Expected Url

def test_verifyTitle(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    mytitle=page.title
    print("Title of the page:",mytitle)
    # expect(page).to_have_title("Automation Testing Practice")