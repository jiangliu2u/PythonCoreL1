def li(func):
    def wrapped(*args,**kwargs):
        return "<b>"+func()+"</b>"
    return wrapped

def h1(func):
    def wrapped(*args,**kwargs):
        return "<h1>"+func()+"</h1>"
    return wrapped

@h1
@li
def say():
    return "hello"

print(say())
