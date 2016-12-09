__author__ = 'jc437351'

stock_file=open("stock.txt","r")
for line in stock_file:
    line = line.strip()
    #print(line)
    split_line = line.split(",")
    print("Name:", split_line[0])
    print("Year:", split_line[1])
    print("Price: ${:.2f}".format(float(split_line[2])))
stock_file.close()

