from contextlib import contextmanager


# notes here must use yield to return a value
@contextmanager
def open_selenium_only():
    driver = None
    try:
        driver = webdriver.Chrome()
        yield driver
    finally:
        if driver is not None:
            driver.quit()
