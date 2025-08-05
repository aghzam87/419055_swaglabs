import pytest
import re
import os

from playwright.sync_api import Page, expect
from pages.homepage import Homepage
from pages.productspage import Productspage
from config import Text 

@pytest.fixture(autouse=True)
def load_homepage(page: Page) -> Homepage:
    page.goto(Text.HOMEPAGE_URL.value, wait_until='load')
    homepage = Homepage(page)
    yield homepage

def login(username, page: Page):
    username = os.getenv(username) 
    # since password is not changing in this demo, not need to pass it
    password = os.getenv("SWAGLAB_PASSWORD")
    if not username or not password:
        raise ValueError("Swaglab username or password environment variables not set.")
    page.login(username, password)

@pytest.mark.testui
def test_swag_labs_to_be_visible(page: Page, load_homepage: Homepage):
    expect(load_homepage.LOGIN_LOGO).to_be_visible()
    expect(load_homepage.LOGIN_LOGO).to_have_text(Text.SWAG_LABS_TITLE.value)

@pytest.mark.testui
def test_swag_labs_login_standard_user(page: Page, load_homepage: Homepage):
    login("SWAGLAB_USERNAME_STANDARD", load_homepage)
    productspage = Productspage(page)
    expect(productspage.page).to_have_url(Text.PRODUCTS_URL.value)
    expect(productspage.PRODUCTS_PAGE_TITLE).to_be_visible()
    expect(productspage.PRODUCTS_PAGE_TITLE).to_have_text(Text.PRODUCTS_PAGE_TITLE.value)

@pytest.mark.testui
def test_swag_labs_login_locked_out_user(page: Page, load_homepage: Homepage):
    login("SWAGLAB_USERNAME_LOCKED", load_homepage)
    # Lockout user stays on the homepage on login attempt
    expect(load_homepage.page).to_have_url(Text.HOMEPAGE_URL.value)
    expect(load_homepage.LOGIN_ERROR_MESSAGE).to_have_text(Text.LOGIN_ERROR_MESSAGE_TEXT.value)