from contextlib import contextmanager
<<<<<<< HEAD
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

=======

@contextmanager
def bob():
    import turtle
    tmp = None
    try:
        tmp = turtle.Turtle()
        yield tmp
    except:
        print("oh noes")
    finally:
        turtle.exitonclick()



with bob() as bob_the_turtle:
    bob_the_turtle.forward(50)
>>>>>>> eda89b5c14893fec229472a0a666eb76b0fbfd01
