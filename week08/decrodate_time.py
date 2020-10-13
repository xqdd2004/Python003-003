'''
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
'''
import time
import random

#自定义实现timer装饰器
def timer(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()

        # 计算运行时间
        cost_time = end_time - start_time
        print(f"函数 {func.__name__} 花费时间：{cost_time:.2f}秒")
    return wrapper

@timer
def test1():
    print('测试1，无参数')
    time.sleep(random.random())

@timer
def test2(name):
    print('测试2，有参数')
    print(f'参数name的值为：{name}')
    time.sleep(random.random())

@timer
def test3(name='geek', type=1):
    print('测试3，有参数')
    print(f'参数name的值为：{name}, type的值为{type}')
    time.sleep(type)

a = test1()
b = test2('test2')
c = test3(name='test3',type=2)
d = test3()

