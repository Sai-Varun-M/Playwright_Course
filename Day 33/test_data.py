import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, Playwright, expect # pyright: ignore[reportMissingImports]

search_items = ['Laptop', 'Gift Card', 'SmartPhone', 'Monitor']

@pytest.mark.parametrize("item", search_items)
def test_data(item, page:Page):
    page.goto("https://demowebshop.tricentis.com/")    
    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()

    first_result = page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item, ignore_case = True)