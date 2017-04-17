from contextlib import contextmanager


# notes here must use yield to return a value
@contextmanager
def open_selenium_only():
    something_cool = None
    try:
        something_cool = 10
        yield something_cool
    except:
        print "you got an error"
    finally:
        print "cleaning up now"


with open_selenium_only() as fake:
    print "hi", fake

    # uncomment below to see the flow
    # raise "NOTHING WORKED"
