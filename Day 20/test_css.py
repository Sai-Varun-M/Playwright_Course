# All combinations to use CSS:- tag id, tag class, tag attribute, tag class attribute

import pytest # pyright: ignore[reportMissingImports]
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

def test_verify_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # tag id - tag#id
    page.locator("input#small-searchterms").fill("T-Shirts")
    page.locator("#small-searchterms").fill("T-Shirts") #Only ID
    page.wait_for_timeout(5000)


    # tag class - tag.class
    page.locator("input.search-box-text").fill("Pants")
    page.wait_for_timeout(5000)


    # tag attribute - tag[attribute=value]
    page.locator("input[name=q]").fill("Shirts")
    page.wait_for_timeout(5000)


    # tag class attribute - tag.class[attribute=value]
    page.locator("input.search-box-text[name=q]").fill("Coats")
    page.wait_for_timeout(5000)