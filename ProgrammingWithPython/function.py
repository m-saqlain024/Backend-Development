def calculate_tax(bill, tax_rate):
    total_tax = (bill * tax_rate) / 100
    return total_tax


print("total Calculate tax :",calculate_tax(1200, 12))
print("total Calculate tax :",calculate_tax(13300, 20))



def result(number):
    if number > 50:
        print("pass")
    else :
        print("faild")

