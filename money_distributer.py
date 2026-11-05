# Get the amount of money from the user
change = float(input("Enter the amount of money as a float: $"))
# Convert the money value into an integer
change = int (change * 100)
print()
print(f"Change Amount: {change / 100:.2f}")
print()
# Determine the amount of coins that will be needed
number_dollars = change // 100
change = change - (number_dollars * 100)
number_quarters = change // 25
change = change - (number_quarters * 25)
number_dimes = change // 10
change = change - (number_dimes * 10)
number_nickels = change // 5
change = change - (number_nickels * 5)
number_pennies = change
if number_dollars > 0:
if number_dollars == 1:
print(f"{number_dollars} Dollar")
else:
print(f"{number_dollars} Dollars")
if number_quarters > 0:
if number_quarters == 1:
print(f"{number_quarters} Quarter")
else:
print(f"{number_quarters} Quarters")
if number_dimes > 0:
if number_dimes == 1:
print(f"{number_dimes} Dime")
else:
print(f"{number_dimes} Dimes")
if number_nickels > 0:
if number_nickels == 1:
print(f"{number_nickels} Nickel")
else:
print(f"{number_nickels} Nickels")
if number_pennies > 0:
if number_pennies == 1:
print(f"{number_pennies} Penny")
else:
print(f"{number_pennies} Pennies")
