from playwright.sync_api import Page, expect
import pytest # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_multidropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#colors").select_option(["Red","Blue","Green"]) #By label
    page.locator("#colors").select_option(label=["Red","Blue","Green"]) 

    page.locator("#colors").select_option(value=["red","white","green"]) #by value

    page.locator("#colors").select_option(index=[4,2]) #by index  

    dropdown_options = page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)