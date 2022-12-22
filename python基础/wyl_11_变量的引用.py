"""
变量的引用：
    变量和数据都是保存在内存中的
    在python中的函数的参数传递以及返回值都是靠引用传递的

在python中：
    变量和数据都是保存在内存中
    数据保存在内存中的一个位置
    变量中保存着数据在内存中的地址

    变量中记录数据的地址，就叫做引用

可变和不可变类型：
    不可变类型：
        数字类型：int bool、float、complex,long(2,x)
        字符串：str
        元组：tuple
    
    可变类型：内存中的数据可以被修改：
        列表：list
        字典：dict
    
    字典中的key 只能是不可变数据类型

哈希（hash):
    python中内置有一个名字叫做hash(o)的函数
        接收一个不可变类型的数据作为参数
        返回结果是一个整数
    哈希是一种算法，其作用就是提取数据的特征码
        相同的内容就得到相同的结果
        不同的内容得到不同的结果

    在pthon中，设置字典的键值对时，会首先对key进行hash已决定如何在内存中保存字典的数据，以后方便后续对字典的操作：增删改查
        键值对的key必须时不可变类型的数据
        键值对的value可以是任意类型的数据
    
    
"""

def test(num):
    print("num:地址%d" % id(num))
    # 定义字符串
    result = "hello"
    print("函数要返回数据的内存地址%d" % id(result))

    # 返回的数据的引用，并不是数据本身
    return result

a = 10
print("a:地址%d" % id(a))
# 调用函数，本质是传递的是实参保存数据的引用，而不是实参保存的数据
r = test(a)
print("函数返回数据的内存地址%d" % id(r))


###################################################


a = 1
a = "hello"

a = [1,2,3]
a = [3,2,1]