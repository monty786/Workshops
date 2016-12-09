__author__ = 'jc437351'
"""
def square_number(num):
    return(num * num)
print(square_number(5))

def is_prime(value):
    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

is_prime(is_prime(5))


"======="
#inch to meter
def inch_to_meter(inch):
    meter = inch/ 39.370
    return meter
inch = float(input("Enter inches:"))
meter = inch_to_meter(inch)
print ("meter:{}".format(meter))

"========"
"""

def tax_return(income):
    tax = 0
    if income > 16000:
        tax=(income -16000) *0.3
    return tax


income =float(input("enter income:$"))
# print(tax_return(income))
tax = tax_return(income)
if tax == 0:
    print("no tax for you")
else:
    print("tax for ${:.2f} income is ${:.2f}".format(income,tax))
