from playwright.sync_api import Page, expect  # pyright: ignore[reportMissingImports]
import re

def test_xpath(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #Absolute xpath
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    #Relative xpath
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

def test_handle_dynamic_elements_css(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    for i in range(5):
        button=page.get_by_role("button",name=re.compile(r'ST.*'))
        button.click()
        page.wait_for_timeout(2000)