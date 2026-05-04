import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_bootstrip(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(3000)

    page.get_by_text("PIM").click()
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(3000)

    options = page.locator("div[role='listbox'] span")

    count = options.count()
    print("Number of options in the dropdown: ",count)
    expect(options).to_have_count(count)
    page.wait_for_timeout(3000)
    print("All the options in the dropdown: ",options.all_text_contents())

    for i in range(count):
        text =options.nth(i).text_content()
        if text == "Automation Tester":
            options.nth(i).click()
            break

    page.wait_for_timeout(5000)