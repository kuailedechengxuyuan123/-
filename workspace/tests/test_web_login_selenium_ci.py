"""Selenium headless login test for CI.

This test is intended for CI (headless) runs. It sets Chrome to headless
mode by default and writes artifacts (screenshot) to the `artifacts/` folder.
"""
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.integration
def test_demo_login_ci():
    # Default to headless in CI runs, allow override via HEADLESS env var
    headless = os.environ.get('HEADLESS', 'true').lower() in ('1', 'true', 'yes')
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    try:
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

        assert driver.execute_script('return document.body.getAttribute("data-auth")') in ('true', True)
    finally:
        out_dir = Path(os.environ.get('ARTIFACTS_DIR', Path(__file__).resolve().parents[1] / 'artifacts'))
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            driver.save_screenshot(str(out_dir / 'selenium_login_ci.png'))
        except Exception:
            pass
        driver.quit()
