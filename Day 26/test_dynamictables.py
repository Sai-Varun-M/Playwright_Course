from playwright.sync_api import Page, expect  # pyright: ignore[reportMissingImports]

def test_dynamic(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table#google_vignette")

    table = page.locator("table.table tbody")

    rows = table.locator("tr").all()

    for row in rows:
        process_name = row.locator("td").nth(0).inner_text()
        if process_name == "Chrome":
            cpu_load = row.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome:", cpu_load)
            break
    
    # expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)
    page.wait_for_timeout(5000)