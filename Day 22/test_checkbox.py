from playwright.sync_api import Page, expect
import pytest # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    check1=page.get_by_label("Sunday")
    check2=page.get_by_label("Saturday")

    expect(check1).to_be_visible()
    expect(check1).to_be_enabled()

    expect(check1).not_to_be_checked()
    check1.check()
    expect(check1).to_be_checked()

    expect(check2).not_to_be_checked()
    check2.check()
    expect(check2).to_be_checked()
    
    page.wait_for_timeout(5000)



def test_check(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes=[]

    checkboxes=[page.get_by_label(day) for day in days ]
    print("Total No. of Checkboxes:",len(checkboxes))

    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()

    page.wait_for_timeout(5000)
