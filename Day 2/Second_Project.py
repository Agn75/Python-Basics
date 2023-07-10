nombre = input("What's your name: ")
incomes = int(input("Please type your income from this month: "))

commision = round(incomes * 13 /100,2)

print(f"You made a total of {incomes}; therefore, you made {commision} in commissions")