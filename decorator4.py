from functools import wraps


def li_label(func):
    @wraps(func)
    def li(*args, **kargs):
        return '<li>' + func() + '</li>'

    return li


def b_label(func):
    @wraps(func)
    def b(*args, **kargs):
        return '<b>' + func() + '</b>'

    return b


@li_label
@b_label
def say_hello():
    return 'Hello'


print(say_hello())
