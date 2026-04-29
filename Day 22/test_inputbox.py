from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_input(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    text_box = page.locator("#name")
    #To check visibility of the elements
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    #check the attribute of the element
    expect(text_box).to_have_attribute("maxlength","15")

    #get an attribute of the element
    maxlength = text_box.get_attribute("maxlength")
    print("Max Lenght:",maxlength)

    text_box.fill("John")

    #Get input value from inputbox
    entered_value = text_box.input_value()
    print("Entered Value is ",entered_value)

    page.wait_for_timeout(5000)