from enum import Enum

class Text(Enum):
    #Titles
    SWAG_LABS_TITLE = "Swag Labs"
    PRODUCTS_PAGE_TITLE = "Products"
    #Button text
    LOGIN_ERROR_MESSAGE_TEXT = "Epic sadface: Sorry, this user has been locked out."
    # URLs
    HOMEPAGE_URL = "https://www.saucedemo.com/"
    PRODUCTS_URL = "https://www.saucedemo.com/inventory.html"
    # Homepage Locators
    LOGIN_LOGO_LOCATOR = ".login_logo"
    USERNAME_LOCATOR = "#user-name"
    PASSWORD_LOCATOR = "#password"
    LOGIN_BUTTON_LOCATOR = "#login-button"
    LOGIN_ERROR_MESSAGE_LOCATOR = ".error-message-container"