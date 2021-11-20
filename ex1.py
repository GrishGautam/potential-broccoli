    
okl = input("enter your name")

good_credit = len(okl)
print(good_credit)

if good_credit <= 3:
    down_payment = "rejected"

elif good_credit >= 50:
    down_payment = "rejected"

else:
    down_payment = "accepted"

print(f'your name is {down_payment} thank you')
