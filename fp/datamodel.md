数据模型，本章主要介绍了python中的特殊方法

len(a_list)的本质分别是返回c语言数据结构的属性（而不是调用函数）

a_list[0]的本质分别是调用类中\_\_getitem\_\_()函数

python中的特殊方法：https://docs.python.org/3/reference/datamodel.html