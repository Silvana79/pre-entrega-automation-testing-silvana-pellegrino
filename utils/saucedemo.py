from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
DEFAULT_TIMEOUT = 10


def wait_for_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def login(driver):
    username_input = wait_for_element(
        driver,
        (By.ID, "user-name")
    )

    password_input = wait_for_element(
        driver,
        (By.ID, "password")
    )

    login_button = wait_for_clickable(
        driver,
        (By.ID, "login-button")
    )

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    login_button.click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.url_contains("/inventory.html")
    )


def get_first_product(driver):
    first_product = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item")
    )

    name = first_product.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    price = first_product.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    return name, price


def add_first_product_to_cart(driver):
    first_product = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item")
    )

    add_button = first_product.find_element(
        By.CLASS_NAME,
        "btn_inventory"
    )

    add_button.click()

    wait_for_element(
        driver,
        (By.CLASS_NAME, "shopping_cart_badge")
    )


def open_cart(driver):
    cart_link = wait_for_clickable(
        driver,
        (By.CLASS_NAME, "shopping_cart_link")
    )

    cart_link.click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.url_contains("/cart.html")
    )
