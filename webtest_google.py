import pytest
import pytest_playwright
import unittest


def test_user_can_search(page):
    page.goto("https://medium.com/search")
    page.click("input[placeholder=\"Search Medium\"]")
    page.fill("input[placeholder=\"Search Medium\"]", "about life")
    page.keyboard.press('Enter')
    page.click("text=/.*25 Things About Life I Wish I .*/")
    page.close()

def test_user_can_clearsearch(page):
    page.goto("https://medium.com/search")
    page.click("input[placeholder=\"Search Medium\"]")
    page.fill("input[placeholder=\"Search Medium\"]", "about life")
    page.getAttribute("input[placeholder=\"Search Medium\"]", "about life")
    page.keyboard.press('Backspace')
    page.getAttribute("input[placeholder=\"Search Medium\"]", "Search Medium")
    page.close()

def test_enter_without_text(page):
    page.goto("https://medium.com/search")
    page.getAttribute("input[placeholder=\"Search Medium\"]", "Search Medium")
    page.keyboard.press('Enter')
    page.getAttribute("input[placeholder=\"Search Medium\"]", "Search Medium")

