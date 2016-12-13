# _*_ coding: utf-8 _*_

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Invaid input')
    else:
        return x

u"默认参数必须指向不变对象"
def addnone(L=[]):
    L.append('END')
    return L

print addnone()
print addnone()

u"可变参数"
def calsum(*nums):
    sum = 0
    for i in nums:
        sum = sum + i
    return sum

print calsum(1, 2, 4)
print calsum(*[1,2,4])

u"关键字参数"
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person("lichee", "21", gender="f", state="happy")

u"参数组合：只能按照必选参数，默认参数，可变参数和关键字参数的顺序来定义参数"
def fucn(a, b, c = 0, *args, **kw):
    print "a = ", a, "b = ", b, 'c =', c, 'args =', args, 'kw =', kw

u"迭代"
d = dict()
d["da"] = 1
d["bu"] = 2
print type(d.keys())
print type(d.iterkeys())
print type(d.itervalues())
print type(d.viewvalues())
print type(d.iteritems())
for value in d.itervalues():
    print value
for item in d.iteritems():
    print item
for item in d.items():
    print item

u"判断是否是可迭代对象"
from collections import Iterable
print isinstance(d.items(), Iterable)

for i, value in enumerate(['a', 'b', 'v']):
    print i, value

u"列表生成式"
print [x + y for x in 'abc' for y in 'xyz']
print [x * x for x in xrange(10) if x % 2 is 0]
a = 'abc'
b = 'xyz'
print [a[i] + b[i] for i in range(3)]
print ['abc'[i] + 'xyz'[i] for i in range(3)]

u"生成器，generator。\
列表元素可以按照算法推算出来，在循环的过程中不断推算出后续的元素-不必创建完整的list，\
从而节省大量的空间。一边循环一边计算."
g = (x * x for x in range(10))
print type(g)
print g.next()
print g.next()
for n in g:
    print 'lala', n
# 试图再次 print g.next() 会报错

u"生成器生成斐波拉契数列："
u"若一个函数定义中包含yield关键字，则该函数即一个generator"
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
print type(fib(6)) # generator
print type(fib) # function

def listn(max):
    n = 0
    while n < max:
        yield n
        n += 1

for i in listn(10):
    print i

name = ['LDI', 'lad']
print map(str.title, name)
print map(str.lower, name)
print map(str.upper, name)
print map(str.capitalize, name)

value = [2, 3, 5]
print reduce((lambda x, y: x * y), value)

u"filter():过滤序列"
def isPrime(num):
    return (0 in map(lambda x: num % x, range(2, num)))
print filter(isPrime, range(1, 101))

u"返回函数与闭包"
def calc_sum(*args):
    return reduce((lambda x, y: x + y), args)
print calc_sum(1, 2, 3, 5)
def lazy_sum(*args):
    def sum():
        return reduce((lambda x, y: x + y), args)
    return sum

f = lazy_sum(1, 2, 4, 19)
print f
print f()

u"返回函数不应该引用任何循环变量， 或者后续会发生变化的量"
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

def count2():
    fs = []
    for i in range(1, 4):
        def f(j = i):
            return j * j
        fs.append(f)
    return fs
f1, f2, f3 = count2()
print f1(), f2(), f3()

def count3():
    for i in range(1, 4):
        def f():
            return i * i
        yield f
for f in count3():
    print f()
