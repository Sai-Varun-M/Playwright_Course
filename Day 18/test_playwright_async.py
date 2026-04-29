from playwright.async_api import Page,expect,async_playwright # pyright: ignore[reportMissingImports]
import pytest  # pyright: ignore[reportMissingImports]

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        mypage= await browser.new_page()
        await mypage.goto("https://testautomationpractice.blogspot.com/") #Passing Url
        await expect(mypage).to_have_url("https://testautomationpractice.blogspot.com/") #Expected Url