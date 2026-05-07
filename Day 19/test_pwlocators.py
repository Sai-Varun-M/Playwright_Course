from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]
import re 
import pytest

@pytest.mark.skip
def test_verify_pwlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    # page.wait_for_timeout(5000) #5000ms = 5 sec

    #get_by_alt_text()
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    #get_by_text()
    mytext=page.get_by_text("Welcome to our store")
    expect(page.get_by_text("Welcome to")).to_be_visible() #Partial Text
    expect(page.get_by_text(re.compile(".*Welcome*."))).to_be_visible() #Partial Text
    expect(mytext).to_be_visible()
    

    #get_by_role()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    expect(page.get_by_role("heading",name="Register")).to_be_visible()

    #get_by_label()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last name").fill("Kenedy")
    page.get_by_label("Email").fill("abc@gmail.com")

    #get_by_placeholder()
    page.get_by_placeholder("Search store").fill("Apple Macbook")
    page.wait_for_timeout(5000)

    #get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")

    #get_by_test_id
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")

@pytest.mark.skip
def test_orangehrm(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    # expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()