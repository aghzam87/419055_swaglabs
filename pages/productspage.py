import pytest
import re

from playwright.sync_api import Page, Locator

class Productspage:

    def __init__(self, page):
        """Few locators just for the purpose of the exercise, a 
         comprehensive test suite will cover all necessary elements and checks"""
        self.page = page
        self.PRODUCTS_PAGE_TITLE: Locator = self.page.locator('.title')