import pytest
import requests


@pytest.mark.integration
def test_web_login_httpbin_basic_auth():
    """Demonstration of a web login-like test against httpbin's basic-auth endpoint.

    This is a simple example of an automated web-login test using requests.
    For real web UI tests use Selenium + webdriver and point to your app under test.
    """
    url = 'https://httpbin.org/basic-auth/user/pass'
    r = requests.get(url, auth=('user', 'pass'))
    assert r.status_code == 200
    j = r.json()
    assert j.get('authenticated') is True
    assert j.get('user') == 'user'
