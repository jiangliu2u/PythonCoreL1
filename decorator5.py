def li(func):
    def wrapped(*args, **kwargs):
        return "<b>" + func() + "</b>"

    return wrapped


def h1(func):
    def wrapped(*args, **kwargs):
        return "<h1>" + func() + "</h1>"

    return wrapped


@h1
@li
def say():
    return "hello"


print(say())


def my_decorator(func_to_decorate):
    def the_wrapper_around_the_func():
        print('Before the function runs')
        func_to_decorate()
        print('After the function runs')

    return the_wrapper_around_the_func


def alone_func():
    print('I am an alone function, hehe!o_O')


alone_func()
alone_func_decorated = my_decorator(alone_func)
alone_func_decorated()


@my_decorator
def another_alone_func():
    print('I am an another alone function, haha!-.-')


another_alone_func()
