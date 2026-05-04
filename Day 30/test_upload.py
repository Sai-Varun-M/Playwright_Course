import pytest  # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

@pytest.mark.skip
def test_upload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#singleFileInput").set_input_files("uploads/test1.txt")
    page.locator("button:has-text('Upload Single File')").click()

    expect(page.locator("#singleFileStatus")).to_contain_text("test1.txt")

    print("File Upload Successful")

    page.wait_for_timeout(3000)


def test_multipleupload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    files = ["uploads/test1.txt","uploads/test2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple File')").click()

    msgloc = page.locator("#multipleFilesStatus")
    expect(msgloc).to_contain_text("test1.txt")
    expect(msgloc).to_contain_text("test2.txt")

    page.wait_for_timeout(3000)
    print("Multiple files uploaded successfully")