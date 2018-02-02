def a_decorator_passing_arguments(func_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print('I got args:', arg1, arg2)
        func_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print('My name is', first_name, last_name)


print_full_name('Liu', 'Jiang')


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # 年龄-3
        return method_to_decorate(self, lie)

    return wrapper


class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print("I am {}, what did you think?".format(self.age+lie))


l = Lucy()
l.sayYourAge(-3)
