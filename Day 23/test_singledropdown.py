from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#country").select_option("India") # By Label Selection
    page.locator("#country").select_option(label="India") #By label Selection

    page.locator("#country").select_option("germany") #by value
    page.locator("#country").select_option(value="germany")

    page.locator("#country").select_option(index=3) #by index


    #check number of options
    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)
    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    #print countries using loop
    for option in options_text:
        print(option)
