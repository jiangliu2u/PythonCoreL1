# python学习笔记
### join的用法 
1. 在python中，默认情况下（其实就是setDaemon(False)），主线程执行完就退出，此时子线程会继续执行直到结束
2. 使用setDaemon(True)方法，设置子线程为守护线程时，主线程执行结束，则全部线程全部被终止执行，可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止。
3. join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止。
4. join有一个timeout参数：当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死该子线程，最后退出程序。所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和。简单的来说，就是给每个子线程一个timeout的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死。
没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，主线程结束，但是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，程序退出。
----
### 单例模式
单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。
\_\_new\_\_()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能有一个实例
1. 使用__new__方法
>     
    class Singleton(object):
        def __new__(cls, *args, **kw):
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            return cls._instance

    class MyClass(Singleton):
        a = 1
2. 共享属性
创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
>     
    class Borg(object):
        _state = {}
        def __new__(cls, *args, **kw):
            ob = super(Borg, cls).__new__(cls, *args, **kw)
            ob.__dict__ = cls._state
            return ob

    class MyClass2(Borg):
        a = 1
3. 装饰器版本
>     
    def singleton(cls, *args, **kw):
        instances = {}
        def getinstance():
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
        return getinstance

    @singleton
    class MyClass:
        ...
4. import方法
作为python的模块是天然的单例模式

>
    # mysingleton.py
    class My_Singleton(object):
        def foo(self):
            pass

    my_singleton = My_Singleton()

    # to use
    from mysingleton import my_singleton

    my_singleton.foo()
     
