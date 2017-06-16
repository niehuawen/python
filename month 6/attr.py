#!/usr/bin/env python
# -- coding:utf-8 --
# hasattr():判断某个对象是否有某个属性
# getattr()：获取某个对象某个属性的值，如果不存在该属性，报AttributeError异常

# 需要继续验证？？？

dicttest = {"a":100,"b":200,"c":300}
if hasattr(dicttest,"keys"):
    print(getattr(dicttest,"keys"))
else:
    print("object {0} has no {1} attribute".format(dicttest,"a"))

