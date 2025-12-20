num_customer = int(input("enter the number of customers."))


def bill_compute(units):
    if units <= 100:
        bill = units * 2.5
    elif units <= 200:
        bill = (100*2.5) + (units - 100)* 3.9
    else:
        bill = (100 * 2.5) + (100 * 3.9) + (units-200)*5.0 
    return bill


for i in range(num_customer):
    print(f"\n customer {i+1}")
    name = input("enter the name of the customer")
    units = float(input("enter the number of units consumed"))

    summation_bill = bill_compute(units)
    print(f"\n Electricity bill for the customer namely {name}: {summation_bill:.2f} rupees")
