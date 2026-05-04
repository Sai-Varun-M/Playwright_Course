import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]
import os

def test_download(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()

    def handle_download(download):
        download.save_as("downloads/testfile.txt")

    page.on("download", handle_download)


    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(3000)

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")
    else:
        print("File not exists")