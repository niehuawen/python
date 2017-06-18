#!/usr/bin/env python
# -- coding:utf-8 --
# 求列表或元组的平均值

while True:
    list1 = []
    while True:
        try:
            rev_str = raw_input("please input a number:")
            if "." in rev_str:
                item = float(rev_str)
            else:
                item = int(rev_str)
            list1.append(item)
        except ValueError as e:
            if rev_str in ("q","Q","quit","exit"):
                break
            print(e)
    # 列表转换为元组
    tuple1 = tuple(list1)
    # 元组元素个数
    tuple1_number = len(tuple1)
    # 元组求和
    tuple1_sum = sum(tuple1)
    # 平均值
    tuple1_avg = float(tuple1_sum)/tuple1_number
    print("average of tuple1 is %s" % (tuple1_avg))

    #控制是否退出求平均值的外层循环
    C_flag = raw_input("Y to Continue,N to Quit.")
    if C_flag == "N":
        break