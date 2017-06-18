#!/usr/bin/env python
# -- coding:utf-8 --
#

# 方式一 显示文件内容
fd = file("2_15.py")
for line in fd:
    print(line),
fd.close()

print("*" * 80)

# 方式二 显示文件内容
with open("2_15.py") as fd:
    for line in fd:
        print(line),

