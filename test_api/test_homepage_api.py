import pytest

from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator
from config import Text

@pytest.fixture(scope = "session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url=Text.HOMEPAGE_URL.value)
    yield request_context
    request_context.dispose()

@pytest.mark.testapi
def test_homepage_api_response_200(api_request_context: APIRequestContext) -> None:
    response = api_request_context.get("")
    assert response.ok
    assert response.status == 200

