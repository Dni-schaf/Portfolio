import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    d = webdriver.Chrome(options=options)
    d.maximize_window()
    yield d
    d.quit()


@pytest.mark.parametrize("user_name", [
"standard_user",
"locked_out_user",
"problem_user",
"performance_glitch_user",
"error_user",
"visual_user"
])
def test_google_search_python(driver, user_name):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    login_name = wait.until(
        EC.visibility_of_element_located((By.NAME, "user-name"))
    )
    login_name.send_keys(user_name)

    login_passwort = wait.until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    login_passwort.send_keys("secret_sauce" + Keys.ENTER)

    inventory_container = wait.until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [item.text for item in items]
    assert any("Sauce Labs Backpack" in name for name in names)
