__author__ = 'jc437351'

def main():
    incomes = []
    num_of_months = int(input("How many num_of_months? "))

    for month in range(1, num_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)


    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:.2f} Total: ${:.2f}".format(month, income, total))


main()

