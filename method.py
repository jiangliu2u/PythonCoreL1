class A(object):
    def foo(self,arg):
        print("this is foo",arg)

    @classmethod
    def foo_cls(cls,arg):
        print("This is class method",arg)

    @staticmethod
    def foo_stc(arg):
        print("This is static method",arg)

A.foo_stc(1)
a =A()
a.foo(2)
a.foo_cls(3)
a.foo_stc(4)
