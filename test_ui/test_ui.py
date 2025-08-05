import pytest
import re
import os

from playwright.sync_api import Page, expect
from pages.homepage import Homepage
from pages.productspage import Productspage
from config import Text 

@pytest.mark.testui

def test_swag_labs_to_be_visible(page: Page):
    homepage = Homepage(page)

    homepage.load()

    expect(homepage.LOGIN_LOGO).to_be_visible()
    expect(homepage.LOGIN_LOGO).to_have_text(Text.SWAG_LABS_TITLE.value)

def test_swag_labs_login_user1(page: Page):
    homepage = Homepage(page)
    productspage = Productspage(page)

    homepage.load()

    username = os.getenv("SWAGLAB_USERNAME_1") 
    password = os.getenv("SWAGLAB_PASSWORD")

    if not username or not password:
        raise ValueError("Swaglab username or password environment variables not set.")
    
    homepage.login(username, password)
    
    expect(productspage.PRODUCTS_PAGE_TITLE).to_be_visible()
    expect(productspage.PRODUCTS_PAGE_TITLE).to_have_text(Text.PRODUCTS_PAGE_TITLE.value)