from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_static(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    rows = table.locator("tr") #count of rows in a table
    expect(rows).to_have_count(7)

    row_count = rows.count()
    print("Number of rows=",row_count)


    columns = rows.locator("th") #Count of columns in a table
    expect(columns).to_have_count(4)

    column_count = columns.count()
    print("Number of rows: ", column_count)


    second_row_cells = rows.nth(2).locator('td') #read all the data from 2nd row of the table
    second_row_texts = second_row_cells.all_inner_texts()
    print("2nd Row Text: ", second_row_texts)
    expect(second_row_cells).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
    for text in second_row_texts:
        print(text)
    
    # read all the data from the table
    all_row_data = rows.all()
    for row in all_row_data[1:]:
        cols = row.locator('td').all_inner_texts()
        print(cols)

    for row in all_row_data[1:]:
        author_name = row.locator('td').nth(1).inner_text()
        if author_name == "Mukesh":
            book_name = row.locator('td').nth(0).inner_text()
            print(f"{author_name} \t {book_name}")