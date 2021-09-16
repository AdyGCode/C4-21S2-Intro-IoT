# ---------------------------------------------------------------------
# Filename      : string-from-list.py
# Location      : ./Session-09
# Project       : Class-Examples
# Author        : Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created       : 16/9/21
# Version       : 0.1
# Description   :
#   This is a description of what the file is for
#
# ---------------------------------------------------------------------
list = ['a', 'b', 'b', 'a']
string = "".join(list)
print(string)

list = ['a', 1, 'b', 2, 'c', 3.141]
string = ''.join(map(str, list))
print(string)

def x2(n):
    return n * 2

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers2 = map(x2, numbers)
for x in numbers2:
    print(x)