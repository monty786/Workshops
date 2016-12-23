__author__ = 'jc437351'

string = input("Text: ")
list = string.split()
repeat = {}
for i in list:
    repeat[i]=list.count(i)

for key in repeat:
    print("{}: {}".format(key,repeat[key]))
