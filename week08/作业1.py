'''
作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.deque
'''

#输出
def  out_print( title,  vlist ):
    print(title)
    for vname in vlist:
        print(vname)

def main():
    list1 = ['list','tuple','dict','collections.deque']
    list2 = ['str','bytes','bytearray','memoryview','array.array']
    list3 = ['list','dict','collections.deque','bytearray','memoryview','array.array']
    list4 = ['str','tuple','bytes']

    out_print('容器序列为：',list1)

    out_print('扁平序列为：',list2 )

    out_print('可变序列为：',list3 )

    out_print( '不可变序列为：',list4 )

if __name__ == '__main__':
    main()