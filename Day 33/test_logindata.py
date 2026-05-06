import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, Playwright, expect # pyright: ignore[reportMissingImports]
import json

login_test_Data = [("laura.taylor1234@example.com", "test123", "valid"),
                   ("invaliduser@example.com", "test321", "invalid"),
                   ("validuser@example.com", "testxyz", "invalid")
                   ]

# file = open("testdata/data.json", "r") #to get data from json files
login_data = json.load(file)

# @pytest.mark.parametrize("email,password,validity", [data["email"],data["password"],data["validity"] for data in login_data])

@pytest.mark.parametrize("email,password,validity",login_test_Data)
def test_login(email, password, validity, page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)

    page.locator("input[value='Log in']").click()

    if validity == "valid":
        logout_link = page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible(timeout = 5000)
    else:
        error_message = page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")