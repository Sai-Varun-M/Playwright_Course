from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown_options = page.locator("#colors>option")
    dropdown2 = page.locator("#animals>option")

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    original_text = options_text.copy()
    sorted_list = sorted(options_text)

    print("Original List:-",original_text)
    print("Sorted list:-",sorted_list)


    options_text2 = [text.strip() for text in dropdown2.all_text_contents()]
    original_text2 = options_text2.copy()
    sorted_list2 = sorted(options_text2)

    print("Original List:-",original_text2)
    print("Sorted list:-",sorted_list2)