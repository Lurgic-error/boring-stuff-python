amount = int(input("Please enter amount\t"))

if amount >= 100:
    print(f'Amount: {amount}')
    print("greater than 100")
elif amount <= 100:
    print(f'Amount: {amount}')
    print("less than 100")

else:
    print(f'Amount: {amount}')
    print("Some amount")