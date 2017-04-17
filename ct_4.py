from contextlib import contextmanager
from selenium import webdriver

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


with open_selenium_only() as driver:
	driver.get("http://google.com")
	import time
	time.sleep(2)

