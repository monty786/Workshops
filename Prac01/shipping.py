__author__ = 'jc437351'

num_of_items = int(input("Number of items : "))
while num_of_items <= 0:
    print("number of items cannot be 0 or -ve please enter again")
    num_of_items = int(input("Number of items : "))
cost_per_item = float(input("Cost per each shipment : $ "))
total_cost = num_of_items * cost_per_item
if total_cost > 100:
    discount = total_cost/10
    total_cost -= discount
print("Total Cost for shipping {} items is $ {}".format(num_of_items,total_cost))
