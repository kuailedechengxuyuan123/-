"""Selenium-based login test example.

This test uses webdriver-manager to automatically install the browser driver.
It opens a simple login demo page and performs login steps.

For local execution ensure `selenium` and `webdriver-manager` are installed and
that a GUI browser (Chrome) is available on the machine.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.integration
def test_demo_login():
    """A demo Selenium test against a simple static login page.

    This script uses a minimal inlined HTML page for demonstration. In real
    projects, point the driver at your application's login URL.
    """
    # Note: For CI/headless runs add options.add_argument('--headless=new') or similar
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    try:
        # Example: use a tiny data URL with a fake login form for offline demo
        html = """
        <html>
        <body>
          <form id='login'>
            <input id='user' name='user' />
            <input id='pass' name='pass' />
            <button id='submit' type='button' onclick="document.body.setAttribute('data-auth', document.getElementById('user').value=='user' && document.getElementById('pass').value=='pass')">Login</button>
          </form>
        </body>
        </html>
        """
        data_url = 'data:text/html;charset=utf-8,' + html
        driver.get(data_url)

        user = driver.find_element(By.ID, 'user')
        passwd = driver.find_element(By.ID, 'pass')
        submit = driver.find_element(By.ID, 'submit')

        user.send_keys('user')
        passwd.send_keys('pass')
        submit.click()

        # simple verification: our inline page sets data-auth attribute to true on success
        assert driver.execute_script('return document.body.getAttribute("data-auth")') in ('true', True)
    finally:
        driver.quit()
