import logging

from selenium.webdriver.common.by import By

from utils.saucedemo import (
    BASE_URL,
    add_first_product_to_cart,
    get_first_product,
    login,
    open_cart,
    wait_for_element,
)

logger = logging.getLogger(__name__)


def test_login_exitoso(driver):
    driver.get(BASE_URL)

    login(driver)

    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"

    products_title = wait_for_element(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert products_title.text == "Products"

    print("Test OK")

    logger.info(
        "Login exitoso. URL actual: %s",
        driver.current_url
    )


def test_catalogo_inventario(driver):
    driver.get(BASE_URL)

    login(driver)

    assert driver.title == "Swag Labs"

    first_product = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item")
    )

    assert first_product.is_displayed()

    product_name, product_price = get_first_product(driver)

    assert product_name.strip() != ""
    assert product_price.startswith("$")

    print(
        f"Primer producto: {product_name} | "
        f"Precio: {product_price}"
    )

    logger.info(
        "Primer producto: %s | Precio: %s",
        product_name,
        product_price
    )

    menu_button = wait_for_element(
        driver,
        (By.ID, "react-burger-menu-btn")
    )

    assert menu_button.is_displayed()

    filter_select = wait_for_element(
        driver,
        (By.CLASS_NAME, "product_sort_container")
    )

    assert filter_select.is_displayed()


def test_carrito_primer_producto(driver):
    driver.get(BASE_URL)

    login(driver)

    product_name, _ = get_first_product(driver)

    add_first_product_to_cart(driver)


    cart_badge = wait_for_element(
        driver,
        (By.CLASS_NAME, "shopping_cart_badge")
    )

    assert cart_badge.text == "1"

    open_cart(driver)

    cart_item = wait_for_element(
        driver,
        (By.CLASS_NAME, "cart_item")
    )

    assert cart_item.is_displayed()

    cart_product_name = cart_item.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    assert cart_product_name == product_name
    