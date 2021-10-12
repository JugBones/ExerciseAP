qty = (int(input("Enter the number of packages purchases: ")))
price = 99

if(qty<10):
    disc = 0
elif(qty<20):
    disc = 0.10
elif(qty<50):
    disc = 0.20
elif(qty<100):
    disc = 0.30
else:
    disc=0.40

subtotal = qty * price
discountamount = disc * subtotal
total = subtotal - discountamount

print("\nDisc amount: $" + format(discountamount, ",.2f") + \
      "\nTotal amount: $" + format(total, ",.2f"))