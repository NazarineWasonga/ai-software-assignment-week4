# selenium_login_test.py
# Automates login (valid + invalid credentials) and records success/failure.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# --- CONFIG: update these ---
LOGIN_URL = "https://example.com/login"  # replace with test site
VALID_USER = "testuser@example.com"
VALID_PASS = "CorrectPassword123"
INVALID_USER = "baduser@example.com"
INVALID_PASS = "WrongPassword"
# CSS/XPath selectors - replace with site's selectors
USER_SELECTOR = "input[name='email']"
PASS_SELECTOR = "input[name='password']"
SUBMIT_SELECTOR = "button[type='submit']"
SUCCESS_CHECK_SELECTOR = "div.profile"  # element present on successful login

# --- SETUP webdriver ---
driver = webdriver.Chrome()  # assumes chromedriver in PATH
driver.implicitly_wait(5)

def run_login_test(username, password):
    driver.get(LOGIN_URL)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, USER_SELECTOR).clear()
    driver.find_element(By.CSS_SELECTOR, USER_SELECTOR).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, PASS_SELECTOR).clear()
    driver.find_element(By.CSS_SELECTOR, PASS_SELECTOR).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, SUBMIT_SELECTOR).click()
    time.sleep(2)
    # Check for success element
    try:
        driver.find_element(By.CSS_SELECTOR, SUCCESS_CHECK_SELECTOR)
        return True
    except:
        return False

if __name__ == "__main__":
    results = {}
    results['valid'] = run_login_test(VALID_USER, VALID_PASS)
    results['invalid'] = run_login_test(INVALID_USER, INVALID_PASS)
    print("Test results:", results)
    # Save screenshot for evidence
    driver.save_screenshot("images/selenium_result.png")
    driver.quit()
