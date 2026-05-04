from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def select_date(page,year,month,date,is_future):
    while True:
        current_month = page.locator(' .ui-datepicker-month').text_content()
        current_year = page.locator(' .ui-datepicker-year').text_content()
        if current_month == True:
            page.locator(' .ui-datepicker-next').click() #for future date
        else:
            page.locator(' .ui-datepicker-prev').click() #for past date
        all_dates = page.locator(".ui-datepicker-calendar td").all()
        for dt in all_dates:
             date_text= dt.inner_text()
             if date_text == date:
                 dt.click()
                 break


def test_date(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    date_input = page.locator("#datepicker")

    #Approach 1
    date_input.fill("10/21/2025")
    expect(date_input).to_have_value("10/21/2025")


    #Approach 2
    # is_future= False
    # date_input.click()
    # select_date(page,"2025","October","15",is_future)
    # expect(date_input).to_have_value("10/15/2025")
    # page.wait_for_timeout(5000)