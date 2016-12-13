# _*_ coding: utf-8 _*_

u"装饰器,decorator,本身即是一个高阶函数"
def log(func):
    def wrapper(*args, **kw):
        print "call %s():" % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print "time"

now()

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print "%s %s():" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log2("execute")
def now():
    print "time"
now()
print now.__name__ # warpper

import functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "%s %s():" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log3("execute")
def now():
    print "time"
now()
print now.__name__ # now

def log4(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "%s %s():" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log4()
def lala():
    print "lla"
@log4("test")
def baba():
    print "bba"
lala()
baba()

u"偏函数，把一个函数的某些参数固定住，返回一个新的，调用起来更方便的函数"
int2 = functools.partial(int, base=2)
print int2('1101')
print int2('2120', base=3)
u"其实是相当于加了一个参数值"
max10 = functools.partial(max, 10)
print max10(2, 5, 6)
