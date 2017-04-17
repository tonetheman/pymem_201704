from contextlib import contextmanager

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
