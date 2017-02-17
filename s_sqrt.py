#!/usr/bin/env python
# -- coding:utf-8 --

#safe_sqrt可以处理负数的平方根
def safe_sqrt(number):
    try:
        import math
        rt = math.sqrt(number)
    except ValueError:
        import cmath
        rt = cmath.sqrt(number)
    finally:
        return rt

if __name__ == "__main__":
    while True:
        try:
            num = float(raw_input("Please input a number:").strip())
        except (ValueError,TypeError),e:
            print("Error reason: %s" % (e))
            break
        else:
            r = safe_sqrt(num)
        if isinstance(r,float):
            print("the root is %.5f of %s" % (r,num))
        else:
            print("the root is %s of %s" % (r,num))