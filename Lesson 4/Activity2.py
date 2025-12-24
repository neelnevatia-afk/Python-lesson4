amount= int(input("Enter the amount: "))
hundred=  amount//100
fifty=(amount%100)//50
ten=((amount%100)%50)//10
print("Number of 100 rupee notes:", hundred)
print("Number of 50 rupee notes:", fifty)   
print("Number of 10 rupee notes:", ten)