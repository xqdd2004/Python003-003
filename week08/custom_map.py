'''
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
'''

#自定义简易版
#参数func传的是一个函数名，可以是python内置的，也可以是自定义的
#参数iterable传的是一个可以迭代的对象，例如列表，元组，字符串这样的
def map(func, *iterable):
    print("调用自定义实现map()函数")
    res = []
    for iter in iterable:
        list1 = []
        for ele in iter:
            list1.append( func(ele) )
        if len(list1) == 0:
            continue
        res.append( list1 )
    return res.__iter__()

#测试函数
def square(x):
    return x*x

#测试样例 
a = map(square, [1,2,3])
b = map(square, [1,2,3],[4,5,6])

c = map(square, {1,2,3})
d = map(square, {1,2,3},{4,5,6})

e = map(square, (1,2,3))
f = map(square, (1,2,3),(4,5,6))



    
    