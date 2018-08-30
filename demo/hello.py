#hello.py
#!/usr/bin/env python
# -*- coding: utf8 -*-

#import os, sys;

print 'hello word';

print 'The quick brown fox', 'jumps over', 'the lazy dog';

print '100 + 200 =', 100 + 200;

print u'请输入:'
#name = raw_input();
name = None

print 'You input:', name;
print '<----------------------------------->'
a = -10
if a >= 0:
    print a
else:
    print -a

print '\\\t\\'
print r'\\\t\\'
print '\'\'line1\\n'
print '''a v b cs d s 
dsa dsa ds  
d sa d sa dsa'''

print '3>2-->', 3>2
print '3>4-->', 3>4

aa = 123 #a is int
print 'aa is', aa
aa = 'ABC' #a is string
print 'aa is', aa

a1 = 'ABCD'
b1 = a1
a1 = 'XYZ!'
print 'b1 is', b1, ',a1 is ', a1
print '10/3 is', 10/3, ',10.0/3 is', 10.0/3, ',10/3.0 is', 10/3.0, ',10.0/3.0 is', 10.0/3.0
print '10%3 is', 10%3

print ord('A')
print chr(65)

translate = u'中文'.encode('utf-8')
'''\xe4\xb8\xad\xe6\x96\x87'''
print translate

print len('\xe4\xb8\xad\xe6\x96\x87')


print u'中文1'.encode('utf-8')
print u'中文2'
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#print '\xc9\xed\xb7\xdd\xd6\xa4'.decode('utf-8')
#print '\xc0\xee\xbd\xdc'.decode('utf-8')

print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%d.' % (u'马克', 1000000)
print '%5d-%04d' % (102, 30)
print '%.2f' % 3.1415926
print 'Age: %s. Gender: %s' % (25, True)
print 'growth rate: %d %%' % 7
print ('\n'.join([' '.join(['%d*%d=%2d' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
classmates = ['Michael', 'Bob', 'Tracy']
for mater in classmates:
    print 'for in loop is', mater

classmates = [u'你', u'是', u'谁']
print classmates
print len(classmates)
classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
classmates.pop(1)
print classmates

#dont have append and insert method in this tuple
classmates_tuple = ('Michael', 'Bob', 'Tracy')
print classmates_tuple
classmates_tuple2 = ('Michael', )
print classmates_tuple2

age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

    
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print u'0-100的奇数和为:', sum

print u'请输入整数:3000'
#birth = int(raw_input('birth: '))
birth = 3000
if birth < 2000:
    print u'00前'
else:
    print u'00后'

#dict==map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
print 'Michael is in dict', 'Michael' in d
print 'Michael1 is not in dict', d.get('Michael1')
print 'Michael1 is not in dict', d.get('Michael1', -1)
s=set([1, 1, 2, 2, 3, 3])
print s
s.add(4)
print s
s.remove(1)
print s

array = ['c', 'b', 'a']
print 'sort array before', array
array.sort()
print 'sort array after ', array
tmp = 'abc'
print 'tmp original data is', tmp
print tmp.replace('a', 'A')
print 'after change tmp, it is', tmp

#def
#空函数
def pop():
    print '''it\'s a empty function''' #不执行打印
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('it\'s not a int or float')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-12)
print my_abs(1000)
#my_abs('a')

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print move(100, 100, 60, math.pi / 6)

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)
print power(5, 2)

#定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=[]): 
#     return L.append('end') #return None
def add_end(L=[]): #will return more None if is used twice
    L.append('END')
    return L

print add_end()
print add_end(), "#wrong"

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END');
    return L
print add_end2()
print add_end2()
print add_end2()

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2, 3, 'a', 'b', x=99)
kw = {'e':'e1', 'd': 'd1'}
func(1, 2, 3, ['a', 'b'], e=kw['e'], d=kw['d'])
func(1, 2, 3, ['a', 'b'], **kw)

args = (1, 2, 3, 4)
kw = {'x': 99, 'y': 'y1'}
func(*args, **kw)
func(1,2,*args, **kw)


#尾递归

def fact_test(n):
    if n is 1:
        return 1
    return n * fact_test(n-1)

def fact_test2(num, product=1):
    if num == 1:
        return product
    return fact_test2(num - 1, num * product)

import timeit

t2 = timeit.Timer('x=range(10)')  
print 'generate 0-9 spend time is', t2.timeit()
v = 5
func1_test = 'fact_test(' + str(v) + ')'
func2_test = 'fact_test2(' + str(v) + ')'

t3=timeit.Timer(func1_test, 'from __main__ import fact_test')
print 'first one is', t3.timeit()
t4=timeit.Timer(func2_test, 'from __main__ import fact_test2')
print 'second one is', t4.timeit()

#run in iPython as below
#timeit fact_test(50)
#timeit fact_test2(50) #需要的运行时间多

#切片
#1, 3, 5, 7, ..., 49
print [x for x in range(1,50, 2)]
L=[x for x in range(1,50)]
print '\n'
print L
print '\n'
print L[:]
print '\n'
print L[:10]
print '\n'
print L[10:20]
print '\n'
print L[10:20:2]
print '\n'
print L[::2]

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
L=(1,2,3,4,5,6,7,)
print L[:-3]
print L[-3:]

from collections import Iterable
print isinstance('abc', Iterable) # str是否可迭代
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代

dict2={"a":"apple","b":"banana","o":"orange"} 
 
print "##########dict######################" 
for i in dict2: 
        print "dict[%s]=" % i,dict2[i] 
 
print "###########items#####################" 
for (k,v) in  dict2.items(): 
        print "dict[%s]=" % k,v 
 
print "###########iteritems#################" 
for k,v in dict2.iteritems(): 
        print "dict[%s]=" % k,v 
 
print "###########iterkeys,itervalues#######" 
for k,v in zip(dict2.iterkeys(),dict2.itervalues()): 
        print "dict[%s]=" % k,v

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

from random import randint
data=[randint(-10, 10) for _ in xrange(10)]
print data
_filter = filter(lambda x:x>=0, data)
print _filter

import os
data=[d for d in os.listdir('.')]
print data

#生成器（Generator）
#生成器都只能用一遍

g=(x for x in range(1, 11)) #g.next() to get the value
for n in g: print n

#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        print 'a is', a, ' b is', b
        n = n + 1
print u'斐波拉契数列--------------------v'
fib(6)

print u'斐波拉契数列----------使用生成器来实现----------v'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print "yield====before==========%d" % n
        yield b #在执行过程中，遇到yield就中断
        print "yield====end==========%d" % n
        a, b = b, a + b
        print 'a is', a, ' b is', b
        n = n + 1
#for d in fib(6): print d

b=fib(6)
print b.next()
print "=============1=============END"
print b.next()
print "=============2=============END"
print b.next()
print "=============3=============END"
print b.next()
print "=============4=============END"
print b.next()
print "=============5=============END"
print b.next()
print "=============6=============END"

#函数式编程，高阶函数
#函数本身也可以赋值给变量，即：变量可以指向函数
#函数名其实就是指向函数的变量

#由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10

#高阶函数，就是让函数的参数能够接收别的函数

# == 比较了两个变量的是否为指向同一个对象

id(123)
#id(object) -> integer
#Return the identity of an object.

#map()和reduce()
#map,对数据进行处理，并返回新的list
def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def f(x,y):
    return x*10+y
print reduce(f, [1,2,4,5,6,7,8])

def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn, map(char2num, '13579'))


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('123456')

#lambda优化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s] #可查询dict api, 可以用int(s)来代替
def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))
print str2int('23560')

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
string = ['adam', 'LISA', 'barT'];
def format(s):
    def split(item):
        return _2upper(item[:1])+_2lower(item[1:])
    def _2lower(l):
        return l.lower()
    def _2upper(u):
        return u.upper()
    return map(split, s)
print 'format------>', format(string)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(l):
    def multip(x,y):
        return x*y
    return reduce(multip, l)
print 'prod multip is---->', prod([1,2,3,4,])

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

#对正整数n，如果用2到sqrt(n)之间的所有整数去除，均无法整除，则n为质数
from math import sqrt
def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(sqrt(n))+1):
        if n%x == 0:
            return False
    return True
print filter(is_prime, [x for x in range(1,101)])

#sorted, 对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
L=[4,65,3,2,87,35]
print sorted(L)

def reversed_cmp(x, y): #倒序
    if x > y :
        return -1
    elif x < y :
        return 1
    else:
        return 0

print sorted(L, reversed_cmp)

s=['bob', 'about', 'Zoo', 'Credit']
print sorted(s) #按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(s, cmp_ignore_case)

#函数作为返回值
#闭包（Closure）

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print 'f1-->', f1, 'value is', f1()
print 'f2-->', f2, 'value is', f2()
print 'f1==f2?', f1 == f2
print 'f1()==f2()?', f1() == f2()

#闭包的缺点
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print 'f1()--->', f1()
print 'f2()--->', f2()
print 'f3()--->', f3()

#解决闭包引起的问题
def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

f1,f2,f3=count()
print 'f1()--2->', f1()
print 'f2()--2->', f2()
print 'f3()--2->', f3()

#匿名函数
#f(n)=x2
"""def f(n):
    return n*n
==lambda x: x * x"""

#lambda x可以理解为匿名函数的参数, :之后为匿名函数的方法体

map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

f = lambda x: x*x
print f(5)

def build():
    return lambda x,y:x*x+y*y
print build()(1,2)


#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
#函数对象有一个__name__属性，可以拿到函数的名字

def now():
    print '2017-02-15'
f=now
print f()

#函数调用前后自动打印日志，但又不希望修改now()函数的定义
import functools #导入模块
def log(func):
    @functools.wraps(func) #为解决func.__name__异常的问题
    def wrapper(*args, **kw):
        print 'called %s() method' % func.__name__
        return func(*args, **kw)
    return wrapper

#@log相当于now = log(now)
@log
def now():
    print '2017-02-15'
now()
print now.__name__


#decorator本身需要传入参数
def log(text):
    def decorator(func):
        @functools.wraps(func) #为解决func.__name__异常的问题
        def wrapper(*args, **kw):
            print '%s %s method' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

#@log('execute')相当于now = log('execute')(now)
@log('execute')
def now():
    print '2013-12-25'

print now()

print now.__name__

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

#写出一个@log的decorator，使它既支持：
"""
@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""


#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
print int('12345')
print int('12345', base=8)
print int('12345', 16)

#default是二进制
def _2toint(x, base=2):
    return int(x, base)
print '\n'
print _2toint('1000000', 10)
print _2toint('1000000')


#import functools
_2toint_ = functools.partial(int, base=2)
print '\n'
print _2toint('1000000')

kw = { 'base': 2 }
print int('10010', **kw)

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10) 
args=(10, 5, 6, 7)
print 'args=(10, 5, 6, 7), MAX is', max2(*args)

print 'max2(5, 6, 7), MAX is', max2(5, 6, 7)

kw={'base':10}
def max2(*args, **kw):
    l = list(args)
    l.append(kw['base'])
    return max(tuple(l))
args=(5, 6, 7)
print max2(*args, **kw)

#模块
#引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
#请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
#而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
#hello2.py

#别名
#Python标准库一般会提供StringIO和cStringIO两个库
#cStringIO是C写的，速度更快
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

#作用域

#正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等

#python第三方库
#https://pypi.python.org/pypi

#pip install whl
#pip install Pillow-2.7.0-cp27-none-win_amd64.whl
#pip install Django


#how to use pillow
from PIL import Image, ImageFilter
try:
    im = Image.open("a.jpg")
    print im.format, im.size, im.mode
    im.thumbnail((200, 100))
    im.save('thumb.jpg', 'JPEG')
except:
    print "Unable to load image"

'''#module
BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SMOOTH
SMOOTH_MORE
SHARPEN'''
#filter
#from PIL import Image, ImageFilter
filter=[ImageFilter.BLUR,ImageFilter.CONTOUR,ImageFilter.DETAIL,ImageFilter.EDGE_ENHANCE,
ImageFilter.EDGE_ENHANCE_MORE,ImageFilter.EMBOSS,ImageFilter.FIND_EDGES,ImageFilter.SMOOTH,ImageFilter.SMOOTH_MORE,ImageFilter.SHARPEN]
im = Image.open("a.jpg")
for index, value in enumerate(filter):
    yy = im.filter(value)
    yy.save("a%s.jpg" % index)
    #yy.show()

#常用的第三方库还有MySQL的驱动：MySQL-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2
#to use "pip list" to review how many module installed
#模块搜索路径
#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

import sys
print sys.path

#如果我们要添加自己的搜索目录
#1, sys.path.append('/Users/michael/my_py_scripts') #这种方法是在运行时修改，运行结束后失效
#2, 设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中

#使用__future__
#find it in __future__

#随后处理

#面向对象编程

#class Student()定义
class Student():
    def __init__(self):
        pass
    def print_score(self):
        print 'test'
        pass

print dir(Student)
#['__doc__', '__init__', '__module__', 'print_score']

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print '<--1-->bart.get_grade is', bart.get_grade()
print '<--2-->lisa.get_grade is', lisa.get_grade()


#class Student(object)定义
print dir(Student)
#['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__',
#'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print_score']


#类和实例
#Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
print bart.age
#print lisa.age #'Student' object has no attribute 'age'

#访问限制
#前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性

#有些时候，你会看到以一个下划线开头的实例变量名，比如__name，这样的实例变量外部是可以访问的，
#但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
#所以，仍然可以通过_Student__name来访问__name变量：

class Student(object):
    def __init__(self, name, score):
        self.__name=name
        self.__score=score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print 'name is', bart.get_name(), 'score is', bart.get_score()
bart.set_score(10)
print bart.get_score()
print 'lisa._Student__name is', lisa._Student__name
lisa.__age = 8
print 'lisa.__age is', lisa.__age
#print 'lisa._Student__age is', lisa._Student__age #'Student' object has no attribute '_Student__age'

#继承和多态
#最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
class Animal(object):
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Dog is eating...'
class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog=Dog()
dog.run()
dog.eat()
cat=Cat()
cat.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print 'a is list?', isinstance(a, list)
print 'b is Animal?', isinstance(b, Animal)
print 'c is Dog?', isinstance(c, Dog)

print 'c is Animal?', isinstance(c, Animal)
print 'b is Dog?', isinstance(b, Dog)

#多态的体现
def run_twice(animal):
    animal.run()

run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print 'Tortoise also is running...'
run_twice(Tortoise())

#“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

class Bee(object):
    def run(self):
        print 'Actually is flying..'
    def sleep(self):
        print 'take a nap..'

run_twice(Bee())
print isinstance(Bee(), Animal) #False
print isinstance(Cat(), Animal) #True

#子类访问父类的属性
class Student(object):
    def __init__(self,name,age,school):
        self.__name = name  # private
        self.__age = age
        self.__school = school

    def say(self):
        print ' my info : ', self.__name , self.__age, self.__school


class Hel(Student):
    def __init__(self,name,age,school):
        super(Hel,self).__init__(name,age,school)

h = Hel('name', 'age', 'school') #h is the instance of Hel
h.say()

class Student(object):
    def __init__(self,name,age,school):
        self.__name = name  # private
        self.__age = age
        self.__school = school

    def say(self):
        print ' my info : ', self.__name , self.__age, self.__school
    #父类中增加获取私有变量的方法        
    def get(self):
        return self.__name,self.__age,self.__school

class Hel(Student):
    #pass #可有可无
    #子类中调用父类中的方法获取私有变量
    def say(self):
        print 'hel info1 %s %s %s'%super(Hel,self).get()
    def say2(self):
        print 'hel info2 %s %s %s'%self.get()
    def say3(self):
        print 'hel info3',self._Student__name , self._Student__age, self._Student__school

h = Hel('name', 'age', 'school') #h is the instance of Hel
h.say()
h.say2()
h.say3()

class Animal(object):
    def run(self):
        print 'Animal is running...'

class People(object):
    def run(self):
        print 'People is running...'

class Man(People, Animal):
    pass
mine=Man()
print mine.run()

class Man(Animal, People): #如果有相同的方法在父类，存在多继承，此时，所以从第一个集成的先找，找到了就运行，找不到就next
    pass
mine=Man()
print mine.run()


#获取对象信息
#使用type()
#判断对象类型，使用type()函数

print type('a')
print type(111)
print type(abs)
print type(h)
print type(None)
print type(False)


import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType

#所有类型本身的类型就是TypeType
print type(int)==type(str)==types.TypeType


#使用isinstance()
#判断class的类型，可以使用isinstance()函数

#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上

#能用type()判断的基本类型也可以用isinstance()判断
#判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode
print u'isinstance()判断 is', isinstance('a', (str, unicode)) and isinstance(u'a', (str, unicode))

#由于str和unicode都是从basestring继承下来的，所以简化后的代码
print isinstance(u'a', basestring)

#使用dir()
dir('abc')
#['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#len('ABC')
#'ABC'.__len__()

#配合getattr()、setattr()以及hasattr()
class MyObject(object):
    def __init__(self, x):
        self.__x__ = x
    def power(self):
        return self.__x__ * self.__x__

obj = MyObject(9)
print 'x', hasattr(obj, 'x')
print '__x__', hasattr(obj, '__x__')
print 'y', hasattr(obj, 'y')
setattr(obj, 'y', 19)
print 'y', hasattr(obj, 'y')
print getattr(obj, 'y')
print getattr(obj, 'z', 404)

#面向对象高级编程

#使用__slots__



#type()
#type()函数可以查看一个类型或变量的类型
#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
#type()函数既可以返回一个对象的类型，又可以创建出新的类型
#也可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print h.hello()
print(type(Hello))
print(type(h))

'''要创建一个class对象，type()函数依次传入3个参数：

1, class的名称；
2, 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3, class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

通过type()函数创建的类和直接写class是完全一样的，
因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class'''

#metaclass
#先定义metaclass，就可以创建类，最后创建实例
#metaclass允许你创建类或者修改类

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

'''
当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。

测试一下MyList是否可以调用add()方法'''

l = MyList()

l.add(1)
print l
l.add(2)
print l

print ur'''ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表'''

class Field(object):
    def __init__(self, name, column_type):
        self.name=name
        self.column_type=column_type
    def __str__(self): #need t return a string
        if self.name is None:
            return ''
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        print 'attrs is ', attrs
        print 'isinstance(attrs, Iterable) is', isinstance(attrs, Iterable)
        for k, v in attrs.iteritems():
            print 'Found mapping: %s==>%s' % (k, v)
            if isinstance(v, Field):
                print 'Found mapping: %s==>%s' % (k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__=ModelMetaclass
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))



class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')



'''
当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找__metaclass__，如果没有找到，
就继续在父类Model中查找__metaclass__，找到了，就使用Model中定义的__metaclass__的ModelMetaclass来创建User类，
也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

在ModelMetaclass中，一共做了几件事情：

1, 排除掉对Model类的修改；

2, 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，
就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误；

3, 把表名保存到__table__中，这里简化为表名默认为类名。

在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。

我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
'''

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

#ModelMetaclass会删除掉User类的所有类属性，目的就是避免造成混淆

#编写程序的时候，千万不要把实例属性和类属性使用相同的名字
class Student(object):
    name = 'Student'

# 创建实例s：
s = Student()
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性：
print(s.name)
Student
# 这和调用Student.name是一样的：
print(Student.name)

# 给实例绑定name属性：
s.name = 'Michael'
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性：
print(s.name)

# 但是类属性并未消失，用Student.name仍然可以访问：
print(Student.name)
# 如果删除实例的name属性：
del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了：
print(s.name)
Student

#pip install autopep8
#format .py file
#autopep8 simple_orm.py -d

#错误、调试和测试
#Python的pdb可以让我们以单步方式执行代码

#错误处理
try:
    print 'try...'
    #r = 10 / 0
    r = 10 / 2
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

print '<==============Except start==============>'
print u'''\n如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句\n'''
value = 5
try:
    print 'try...'
    r = 10 / int(value)
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

print u'''Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，
它不但捕获该类型的错误，还把其子类也“一网打尽”'''

try:
    #foo()
    r = 10 / int('a')
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'

print u'''Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看下面\n'''
print '''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
       +-- ImportWarning
       +-- UnicodeWarning
       +-- BytesWarning
\n'''

print u'''使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如:
函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理\n'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'StandardError show!'
    finally:
        print 'finally...'

main()


#调用堆栈
print u'''如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py'''
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

#main()

#记录错误
print u'''Python内置的logging模块可以非常容易地记录错误信息'''

import logging
# err.py
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

#抛出错误
print u'''\n如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例\n'''

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == (0):
        raise FooError('invalid value %s: ' % s)
    return 10/n

#foo(0)
foo(2)

print u'''\nraise还可以往上抛错误\n'''
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main(s):
    bar(s)

main(2)

print u'''\nraise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型\n'''
def foo(s):
    try:
        print 10.0000 / s
    except ZeroDivisionError:
        raise ValueError('input error!')
def main(s):
    try:
        foo(s)
    except ZeroDivisionError, e:
        print 'Exception catch a error, here--->', e
    else:
        print 'else clause when no error is catched.....'
    finally:
        print 'finally function.....'
main(4)

#调试(print, assert, logging, pdn)

print u'''\nassert语句本身就会抛出AssertionError\n'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #!False
    print 'n is not 0 or letter'
    return 10 / n

def main():
    print foo(2)
    #print foo(0)
    #print foo('s')
main()

#可以用-O参数来关闭assert


#logging
print u'''\n在import logging之后添加一行配置logging.basicConfig(level=logging.INFO),再试试\n'''
logging.basicConfig(level=logging.INFO)
s = 1 #'0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

print u'''\n这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。\n'''


#pdb
print u'''\n启动Python的调试器pdb，让程序以单步方式运行\n'''
print u'''\n
python -m pdb err.py
输入命令l来查看代码
输入命令n可以单步执行代码
输入命令p 变量名来查看变量
输入命令q结束调试
\n'''

print u'''\n运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行\n'''

import pdb

s = 1 #'0'
n = int(s)
#pdb.set_trace() # 运行到这里会自动暂停
print 10 / n

#单元测试

print u'''TDD：Test-Driven Development'''

#setUp与tearDown
#分别在每调用一个测试方法的前后分别被执行

"""
单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
"""



#文档测试
import re
m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)


#正则表达式
#https://docs.python.org/2/howto/regex.html#repeating-things
#http://www.cnblogs.com/chuxiuhong/p/5885073.html
#http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html


#IO编程
#文件读写
f = None
try:
    f = open('./frame.py', 'r')
    print f.read()
except IOError, e:
    print 'have an IOError', e
finally:
    if f:
        f.close()

print '''use with to automatically close io stream\n'''
with open('./frame.py', 'r') as f:
    print f.read() #read all content of file


#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('./frame.py', 'r') as f:
    i=0
    for line in f.readlines():
        i=i+1
        print 'L%d' %i, line.strip() # 把末尾的'\n'删掉


#file-like Object
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲

#二进制文件
f = open('./a.jpg', 'rb')
#print f.read()

#字符编码
with open('./gbk.txt', 'r') as f:
    print f.read().decode('gbk')

#with open('./process_thread/threadTest.py', 'w') as f:
#    print f.read().decode('utf-8')

#读文件时自动转换编码，直接读出unicode
import codecs
with codecs.open('./gbk.txt', 'r', 'gbk') as f:
    print f.read() # u'\u6d4b\u8bd5'

#写文件
with codecs.open('./gbk2.txt', 'wb', 'gbk') as f:
    f.write(u'写入如下信息')
    print u'写入成功'

#操作文件和目录
import os
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print os.name
#os.uname()函数在Windows上不提供

#环境变量
print os.environ
print os.getenv('PATH')

#操作文件和目录
print u'操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中'
print u'当前文件的绝对路径', os.path.abspath('.')
#print u'在当前目录下创建一个文件夹', os.mkdir(os.path.join('./', 'testdir'))
#print u'在当前目录下删除某个文件夹', os.rmdir('C:\\Users\\Jaylee\\Documents\\Tencent Files\\121769651\\FileRecv\\MobileFile\\Image')


print os.path.split('./hello.py')
print os.path.splitext('./hello.py')
#print 'rename file',  os.rename('test.txt', 'test.py')
#print 'remove file',  os.remove('test.py')

import shutil
#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

print 'file filter', [x for x in os.listdir('.') if os.path.isdir(x)]
print 'list all end with .py file here', [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#task, 编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径

#序列化(Python中叫pickling)

print u'''Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，
区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
用的时候，先尝试导入cPickle，如果失败，再导入pickle'''

try:
    import cPickle as pickle
except ImportError:
    import pickle

print u'序列化'
d = dict(name='Bob', age=20, score=88)
f=None
try:
    f = open('./dump.txt', 'wb')
    pickle.dump(d, f) #把任意对象序列化成一个str
except IOError, e:
    print 'has IOError issue'
finally:
    if f:
        f.close()

print u'反序列化'

f=None
try:
    f = open('./dump.txt', 'rb')
    d = pickle.load(f) #把任意对象序列化成一个str
    print d
except IOError, e:
    print 'has IOError issue'
finally:
    if f:
        f.close()

#notice, 可能不同版本的Python彼此都不兼容，只能用Pickle保存那些不重要的数据

#JSON
print u'''\n
JSON类型    Python类型
{}          dict
[]          list
"string"    'str'或u'unicode'
1234.56     int或float
true/false  True/False
null        None'''


import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

print u'''反序列化得到的所有字符串对象默认都是unicode而不是str。
由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换'''

print u'JSON进阶'

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)

print json.dumps(s, default=student2dict)
print(json.dumps(s, default=lambda s: s.__dict__))

print u'把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例'
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student, encoding='utf-8'))


#进程和线程

#多进程

print 'Process (%s) start...' % os.getpid()
pid=0
try:
    #每当有新的http请求时，就fork出子进程来处理新的http请求
    pid = os.fork() #this internal method is for mac, linux OS only
except BaseException, e:
    print 'this line code works on mac os only, have python issue'
finally:
    if pid==0:
        print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getpid()+1) #os.getppid(), only work on mac, linux
    else:
        print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

#multiprocessing
#Process, Pool, Queue, 
#进程间通信
print u'''多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
互不影响，而多线程中，所有变量都由所有线程共享\n'''
print u''' GIL 锁：Global Interpreter Lock，任何 Python 线程执行前，必须先获得 GIL 锁，然后，
每执行 100 条字节码，解释器就自动释放 GIL 锁，让别的线程有机会执行。
这个 GIL 全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在 Python 中只能交替执行，即使 100 个线程跑在 100核 CPU 上，
也只能用到 1 个核。\n'''

print u'''Python 虽然不能利用多线程实现多核任务，但可以通过多进程实
现多核任务。多个 Python 进程有各自独立的 GIL 锁，互不影响\n'''

print u'ThreadLocal解决同意变量频繁传递问题\n'
print u'''ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP 请求，
用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。'''

def  process_student(name):
    std = Student(name)
    # std 是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)
def  do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)
def  do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)


global_dict = {}
def  std_thread(name):
    std = Student(name)
    # 把 std 放到全局变量 global_dict 中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()
def  do_task_1():
    # 不传入 std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
def  do_task_2():
    # 任何函数都可以查找出当前线程的 std 变量：
    std = global_dict[threading.current_thread()]


import time, threading
# 创建全局 ThreadLocal 对象:
local_school = threading.local()
def  process_student():
    print 'Hello, %s (in %s)\n' % (local_school.student, threading.current_thread().name)
    time.sleep(0.1)
def  process_thread(name):
    # 绑定 ThreadLocal 的 student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t3 = threading.Thread(target= process_thread, args=('Jay',), name='Thread-C')
t4 = threading.Thread(target= process_thread, args=('Lancer',), name='Thread-D')
t4.start()
t1.start()
t2.start()
t3.start()

t3.join()
t4.join()
t1.join()
t2.join()

print u'进程 vs. 线程\n'


print u'正则表达式'


print re.split(r'\s+', 'a b c')

print re.split(r'[\s\,]+', 'a,b, c d')

print re.split(r'[\s\,\;]+', 'a,b;; c d')

print u'用 () 表示的就是要提取的分组（Group）'

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

print u' group(0) 永远是原始字符串'
print 'group(0)', m.group(0)
print 'group(1)', m.group(1)
print 'group(2)', m.group(2)

t = '19:05:30'
print 'time is ', t
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

print r'groups()-->', m.groups()

print u'正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符'

print u'贪婪匹配'
print re.match(r'^(\d+)(0*)$', '102300').groups()

print u'非贪婪匹配'
print re.match(r'^(\d+?)(0*)$', '102300').groups()

print u'预编译该正则表达式, compile, 如果要多次使用'

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print re_telephone.match('010-12345').groups()

print re_telephone.match('010-808').groups()

u'''
请尝试写一个验证 Email 地址的正则表达式。版本一应该可以验证出类似的 Email：
someone@gmail.com
bill.gates@microsoft.com
版本二可以验证并提取出带名字的 Email 地址：
<Tom Paris> tom@voyager.org\n'''

email = re.compile('[^\.-][\w\.-]+[@]{1}[A-Za-z]+[.]{1}[A-Za-z]+$')
#email = re.compile('[^\.-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')

print 'someone@gmail.com-->match', email.match('someone@gmail.com').group()
print 'bill.gates@microsoft.com-->match', email.match('bill.gates@microsoft.com').group()


print u'常用内建模块'

print u'模块-->collections-->namedtuple'

from collections  import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print 'p.x=%s' % p.x, 'p.y=%s' % p.y

print 'isinstance(p, Point)', isinstance(p, Point)

Circle = namedtuple('Circle', ['x', 'y', 'r'])

c=Circle(1,2,3)

print 'c.x=%s' % c.x, 'c.y=%s' % c.y, 'c.r=%s' % c.r

print 'isinstance(c, Circle)', isinstance(c, Circle)

print u'deque 是为了高效实现插入和删除操作的 双向列表，适合用于队列和栈'

from collections  import deque

q = deque(['a', 'b', 'c'])

q.append('x')
q.appendleft('y')

print 'append-->', q

q.pop()
q.popleft()

print 'pop-->', q

print u'''使用 dict 时，如果引用的 Key 不存在，就会抛出 KeyError 。
如果希望 key 不存在时，返回一个默认值，就可以用 defaultdict '''

from collections  import defaultdict

d=defaultdict(lambda: 'N/A')
d['key1']='value1'

print 'd[\'key1\'] value is ->', d['key1']
print 'd[\'key2\'] value is ->', d['key2']

print u'''我们无法确定 Key 的顺序。
如果要保持 Key 的顺序，可以用 OrderedDict'''

from collections  import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])

print 'no order-->', d

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print 'order-->', od

print u' OrderedDict 的 Key 会按照插入的顺序排列，不是 Key 本身排序'

od = OrderedDict()

od['x']=1
od['z']=3
od['y']=2

print 'after insert data to orderedDict', od

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        print 'before update, self--->', self
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)
        print 'after update, self--->', self

fifo=LastUpdatedOrderedDict(3)
fifo.__setitem__('key1', 'val1')
fifo.__setitem__('key3', 'val3')
fifo.__setitem__('key2', 'val2')
fifo.__setitem__('key4', 'val4')

print u'Counter 是一个简单的计数器，例如，统计字符出现的个数'

from collections  import Counter

c = Counter()

for ch  in 'programming':
    print 'ch is -->', ch
    c[ch] = c[ch] + 1

print c

print u'Base64 是一种最常见的二进制编码方法'

print u'''Base64 编码会把 3 字节的二进制数据编码为 4 字节的文本数据，长度增加 33%，好
处是编码后的文本数据可以在邮件正文、网页等直接显示。'''

print u'''如果要编码的二进制数据不是 3 的倍数，最后会剩下 1 个或 2 个字节怎么办？Base64 用 \
x00 字节在末尾补足后，再在编码的末尾加上 1 个或 2 个 = 号，表示补了多少字节，解码的
时候，会自动去掉'''

import base64

pwd=base64.b64decode('MDA1bWNyAA==')

print base64.b64decode("eyJzaWduIjoidHJ1ZSIsInB3ZCI6Ik5qRXdOVEkzTVRrNE9URXdNVEl6TWpVeGZpVithbUZzT0RreE1 \
    ERXkiLCJ1c2VydHlwZSI6ImdlcmVuIiwibmljaGVuZyI6IkpheWxlZSIsInpoZW5nam\
    lhbmxlaXhpbmciOiLJ7bfd1qQiLCJ6aGVuZ2ppYW5oYW8iOiI2MTA1MjcxOTg5MTAxMjMyNTEiLCJ4aW5nbWluZyI6IsDuvdwifQ==")

print 'password is %d, it\'s -->%s<--' % (len(pwd), pwd)

print base64.b64encode('binary\x00string')

print base64.b64decode('YmluYXJ5AHN0cmluZw==') # has issue

print len('YmluYXJ5AHN0cmluZw==')

print u'''由于标准的 Base64 编码后可能出现字符 + 和 / ，在 URL 中就不能直接作为参数，所以又有
一种"url safe"的 base64 编码，其实就是把字符 + 和 / 分别变成 ‐ 和 _ '''

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')

print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')

print base64.urlsafe_b64decode('abcd--__')

print u'请写一个能处理去掉 = 的 base64 解码函数'

print base64.b64decode('YWJjZA==')

def safe_b64decode(val='YWJjZA'):
    result = None
    try:
        result = base64.b64decode(val)
        return result
    except TypeError, msg:
        print 'msg is ', msg
        val += '==='
        print 'val is', val
        return safe_b64decode(val)
    #finally:
    #    return result



result=safe_b64decode()
print 'result is -->', result

print u'Python 提供了一个 struct 模块来解决 str 和其他二进制数据类型的转换'

print u'> 表示字节顺序是 big-endian，也就是网络序， I 表示 4 字节无符号整数'

import struct

print struct.pack('>I', 10240099)

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

file_size = None
#with open('./python-images.bmp', 'r') as f:
#    file_size = f.read()

f = None
try:
    f = open('./python-images.bmp', 'r')
    file_size = f.read()
except IOError, e:
    print 'have an IOError', e
finally:
    if f:
        f.close()

print file_size #有问题
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print struct.unpack('<ccIIIIIIHH', s)

#hashlib-->MD5，SHA1

import hashlib

print u'''MD5 是最常见的摘要算法，速度很快，生成结果是固定的 128 bit 字节，通常用一个 32 位
的 16 进制字符串表示'''

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

md5_1 = hashlib.md5()
md5_1.update('how to use md5 in ')
md5_1.update('python hashlib?')
print md5_1.hexdigest()
print u'SHA1 的结果是 160 bit 字节，通常用一个 40 位的 16 进制字符串表示'
sha1 = hashlib.sha1()
sha1.update('how to use md5 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

print u'SHA256'
sha256 = hashlib.sha256()
sha256.update('how to use md5 in ')
sha256.update('python hashlib?')
print sha256.hexdigest()

print u'SHA512'
sha512 = hashlib.sha512()
sha512.update('how to use md5 in ')
sha512.update('python hashlib?')
print sha512.hexdigest()

print u'SHA512'
sha512 = hashlib.sha512()
sha512.update('how to use md5 in ')
sha512.update('python hashlib?')
print sha512.hexdigest()

print u'hash file as sha512'
sha512 = hashlib.sha512()
sha512.update(file_size)
print sha512.hexdigest()

#itertools

print u'count() 会创建一个无限的迭代器，所以上述代码会打印出自然数序列'

import itertools
natuals = itertools.count(1)
for n in natuals:
    if n == 5:
        break
    print n
    
print u'cycle() 会把传入的一个序列无限重复下去'

cs = itertools.cycle('ABC')
cs_len = len('ABCD')
i = 0
for c in cs:
    if cs_len == i:
        break
    print c
    i+=1

print u'repeat() 负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数'

ns = itertools.repeat('A', 10)

i = 0
for n in ns:
    if 10 == i:
        break
    print n

print u'takewhile() 等函数根据条件判断来截取出一个有限的序列'

natuals = itertools.count(1)

ns = itertools.takewhile( lambda x: x <= 10, natuals)

for n in ns:
    print n

print u'chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器'

for c in itertools.chain('ABC', 'XYZ'):
    print c

print u'groupby() 把迭代器中相邻的重复元素挑出来放在一起'

for key, group  in itertools.groupby('AAABBBCCAAA'):
    print key, group
    print key, list(group)

for key, group  in itertools.groupby('AaaBBbcCAAa',  lambda c: c.upper()):
    print key, group
    print key, list(group) #list功能，需要熟悉，有问题（仅仅作为标注，代码没问题）

print u'imap() 和 map() 的区别在于，imap() 可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准'

for x  in itertools.imap( lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x

print u'imap() 返回一个迭代对象，而 map() 返回 list。当你调用 map() 时，已经计算完毕'

r = map( lambda x: x*x, [1, 2, 3])

print r

r = itertools.imap(lambda x: x*x, itertools.count(1))

for n in itertools.takewhile(lambda x: x<100, r):
    print n

#r = map(lambda x: x*x, itertools.count(1)) #死循环
#print r

print u'ifilter() 就是 filter() 的惰性实现'

print u'''itertools 模块提供的全部是处理迭代功能的函数，它们的返回值不是 list，而是迭代对象，
只有用 for 循环迭代的时候才真正计算'''

#XML

print u'''操作 XML 有两种方法：DOM 和 SAX。DOM 会把整个 XML 读入内存，解析为树，因此占
用内存大，解析慢，优点是可以任意遍历树的节点。SAX 是流模式，边读边解析，占用内
存小，解析快，缺点是我们需要自己处理事件'''


print u'在 Python 中使用 SAX 解析 XML 非常简洁，通常我们关心的事件是 start_element ， end_element 和 char_data'

print u'生成XML'

import base64

base64.b64encode('i\xb7\x1d\xfb\xef\xff')

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(base64.b64encode('some & data'))
L.append(r'</root>')
print ''.join(L)

print u'''练习一下解析 Yahoo 的 XML 格式的天气预报，获取当天和最近几天的天气：
http://weather.yahooapis.com/forecastrss?u=c&w=2151330
参数 w 是城市代码，要查询某个城市代码，可以在 weather.yahoo.com 搜索城市，浏览器
地址栏的 URL 就包含城市代码。'''


#how to use pillow
from PIL import Image, ImageFilter
try:
    im = Image.open(u"./images/风景.jpg")
    print im.format, im.size, im.mode
    w, h = im.size
    im.thumbnail((w/2, h/2))
    im.save(u'./images/风景_thumb.jpg', 'JPEG') #乱码问题
except:
    print "Unable to load image"

print u'生成验证码'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def  rndChar():
    return chr(random.randint(65, 90))
# 随机颜色 1:
def  rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色 2:
def  rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建 Font 对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建 Draw 对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x  in range(width):
    for y  in range(height):
        draw.point((x, y), fill=rndColor())

# 输出文字:
for t  in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)

image.save('code.jpg', 'jpeg');

print u'详情，请学习http://effbot.org/imagingbook/'

print u'图形界面'

print u'Python 支持多种图形界面的第三方库, Tk(Tkinter自带), wxWidgets, Qt, GTK'

print u'网络编程'

print u'TCP 编程, Socket'

print u'UDP 编程, 使用 UDP 协议时，不需要建立连接，只需要知道对方的 IP 地址和端口号'

print u'服务器绑定 UDP 端口和 TCP 端口互不冲突'

print 'email...'


print 'download...'
#https://mule-studio.s3.amazonaws.com/6.2.2-U2/AnypointStudio-for-win-64bit-6.2.2-201701271427.zip






























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































