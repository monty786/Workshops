__author__ = 'jc437351'
choice = int(input("Enter a +ve/-ve value :"))
sale = float(input("Enter your sale: $"))

while choice >= 0:
    if sale<1000:
        bonus= 10/100*sale
        print("your bonus is: ",bonus)
    elif sale>=1000:
        bonus= 15/100*sale
        print("your bonus is:",bonus)
    choice = int(input("Enter a +ve/-ve valueEnter a +ve/-ve value: "))
print("thank you")
