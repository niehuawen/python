#!/usr/bin/env python
# -- coding:utf-8 --
# while 和 for 求列表和元组的和

# 用户输入元素组成列表,由于元组不可变，不能逐个添加至元组，通过列表转换为元组的方式实现元组的用户输入
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
# 列表和元组显示
print(list1)
tuple1 = tuple(list1)
print(tuple1)

list1_len = len(list1)
tuple1_len = len(tuple1)

list1_index = 0
tuple1_index = 0
list1_sum = 0
tuple1_sum = 0

while list1_index < list1_len:
    list1_sum += list1[list1_index]
    list1_index += 1
print("sum of list1 is %s" %(list1_sum))
    
while tuple1_index < tuple1_len:
    tuple1_sum += tuple1[tuple1_index]
    tuple1_index += 1
print("sum of tuple1 is %s" %(tuple1_sum))

list2_sum = 0
for item in list1:
    list2_sum += item
print("sum of list1 is %s" %(list2_sum))