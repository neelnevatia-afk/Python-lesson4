c=float(input("Enter The Cost Price of the Product: "))
s=float(input("Enter The Selling Price of the Product: "))
if c > s:
    print("Loss")
elif c < s:
    print("Profit")
else:
    print("No Profit No Loss")