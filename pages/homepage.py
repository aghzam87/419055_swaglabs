import pytest
import re

from playwright.sync_api import Page, Locator
from dotenv import load_dotenv
from config import Text

load_dotenv() # Load credentials securely from .env file

class Homepage:

    def __init__(self, page):
        """Few locators just for the purpose of the exercise, a 
         comprehensive test suite will cover all necessary elements and checks"""
        self.page = page
        self.LOGIN_LOGO: Locator = self.page.locator(Text.LOGIN_LOGO_LOCATOR.value)
        self.USERNAME: Locator = self.page.locator(Text.USERNAME_LOCATOR.value)
        self.PASSWORD: Locator = self.page.locator(Text.PASSWORD_LOCATOR.value)
        self.LOGIN_BUTTON: Locator = self.page.locator(Text.LOGIN_BUTTON_LOCATOR.value)
        self.LOGIN_ERROR_MESSAGE: Locator = self.page.locator(Text.LOGIN_ERROR_MESSAGE_LOCATOR.value)

    def login(self, username, password):
        self.USERNAME.fill(username)
        self.PASSWORD.fill(password)
        self.LOGIN_BUTTON.click()