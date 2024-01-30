import pytest

from driver import Driver


@pytest.fixture(autouse=True)
def browser() -> Driver:
    driver = Driver(executable_path="path/to/driver")
    driver.set_window_size(1920, 1080)
    driver.get("https://habr.com/ru/all")

    yield driver

    try:
        driver.quit()
    finally:
        driver.__class__._instances = {}