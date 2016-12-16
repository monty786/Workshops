__author__ = 'jc437351'


num = 0
out_file = open("number.txt","w")
while num >= 0:
    num = int(input("number: "))
    if num >= 0:
        print(str(num),file=out_file)
out_file.close()
