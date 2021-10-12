#enter your bill
subtotal = int(input("Enter the subtotal: "))
tip = int(input("Enter tip amount(as a %): "))

#formula
tip_amt = subtotal * tip/100
total = subtotal + tip_amt

#result
print(f"\nsubtotal : ${subtotal:,.2f}")
print(f"tip : ${tip_amt:,.2f}")
print(f"total : ${total:,.2f}\n")
