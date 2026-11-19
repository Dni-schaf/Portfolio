import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


def maybe_handle_cookie_banner(driver):
    wait = WebDriverWait(driver, 3)  # kürzer, weil optional
    try:
        options = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button//div[text()='Optionen verwalten']")
            )
        )
        options.click()

        confirm = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button//div[text()='Auswahl bestätigen']")
            )
        )
        confirm.click()
    except TimeoutException:
        pass

@pytest.fixture
def driver():
    options = Options()
    d = webdriver.Chrome(options=options)
    d.maximize_window()
    yield d
    d.quit()


def test_automationexercise(driver):
    driver.get("http://automationexercise.com")
    maybe_handle_cookie_banner(driver)

    wait = WebDriverWait(driver, 10)

    options = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button//p[normalize-space(text())='Optionen verwalten']")
        )
    )
    options.click()

    confirm = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button//p[normalize-space(text())='Auswahl bestätigen']")
        )
    )
    confirm.click()

    login_link = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a[href='/login']")
        )
    )
    login_link.click()

    signup_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='signup-name']")
        )
    )
    signup_name.send_keys("Testuser2026")

    signup_email = driver.find_element(
        By.CSS_SELECTOR,
        "input[data-qa='signup-email']"
    )
    signup_email.send_keys("Testuser2026@web.de" + Keys.ENTER)

    form_container = wait.until(
        EC.visibility_of_element_located((By.ID, "form")
        )
    )
    assert "ENTER ACCOUNT INFORMATION" in form_container.text
    time.sleep(3)

    driver.execute_script("""
        const el = document.querySelector('div.grippy-host');
        if (el) el.remove();
    """)

    password = driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']")
    password.send_keys("123456")

    day_select_element = driver.find_element(By.CSS_SELECTOR, "select[data-qa='days']")
    day_select = Select(day_select_element)
    day_select.select_by_value("15")

    month_select_element = driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']")
    month_select = Select(month_select_element)
    month_select.select_by_value("6")

    year_select_element = driver.find_element(By.CSS_SELECTOR, "select[data-qa='years']")
    year_select = Select(year_select_element)
    year_select.select_by_value("1999")

    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    if not newsletter_checkbox.is_selected():
        newsletter_checkbox.click()

    partner_checkbox = driver.find_element(By.ID, "optin")
    if not partner_checkbox.is_selected():
        partner_checkbox.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "input[data-qa='first_name']")
    first_name.send_keys("test")

    last_name = driver.find_element(By.CSS_SELECTOR, "input[data-qa='last_name']")
    last_name.send_keys("user")

    address = driver.find_element(By.CSS_SELECTOR, "input[data-qa='address']")
    address.send_keys("teststreet")

    country_element = driver.find_element(By.CSS_SELECTOR, "select[data-qa='country']")
    country = Select(country_element)
    country.select_by_value("New Zealand")

    state = driver.find_element(By.CSS_SELECTOR, "input[data-qa='state']")
    state.send_keys("teststate")

    city = driver.find_element(By.CSS_SELECTOR, "input[data-qa='city']")
    city.send_keys("testcity")

    zipcode = driver.find_element(By.CSS_SELECTOR, "input[data-qa='zipcode']")
    zipcode.send_keys("12345")

    mobile_number = driver.find_element(By.CSS_SELECTOR, "input[data-qa='mobile_number']")
    mobile_number.send_keys("123456789")

    time.sleep(3)

    create_account_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    create_account_button.click()





