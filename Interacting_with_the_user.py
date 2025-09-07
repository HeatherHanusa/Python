"""
Requirements:
Design a python program that prompts users to enter their total budget (ask them for their net monthly income) and amounts for spending categories:
housing (rent or mortgage) Utilities Groceries Transportation Heath Care Personal Care Clothing, and Debt
"""
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area of the rectangle is: {area:.2f}")

Income = float(input("Enter your monthly income: "))
Housing = float(input("Enter your monthly Housing cost (rent or mortgage: "))
Utilities = float(input("Enter your monthly Utilities cost: "))
Groceries = float(input("Enter your monthly Groceries cost: "))
Transportation = float(input("Enter your monthly Transportation cost: "))
Health_Care = float(input("Enter your monthly Health Care cost: "))
Personal_Care = float(input("Enter your monthly Personal Care cost: "))
Clothing = float(input("Enter your monthly Clothing cost: "))
Debt = float(input("Enter your monthly Debt cost: "))
"Calculate the percentage of the total budget spent in each category"
print(f"The percentage of Housing is{(Housing/Income)*100: .2f}%")
print(f"The percentage of Utilities is{(Utilities/Income)*100: .2f}%")
print(f"The percentage of Groceries is{(Groceries/Income)*100: 2f}%")
print(f"The percentage of Transportation is{(Transportation/Income)*100: .2f}% ")
print(f"The percentage of Health Care is{(Health_Care/Income)*100: .2f}%")
print(f"The percentage of Personal Care is{(Personal_Care/Income)*100: .2f}%")
print(f"The percentage of Clothing is{(Clothing/Income)*100: .2f}%")
print(f"The percentage of Debt is{(Debt/Income)*100: .2f}%")   


"Total spending"
print(f"Your total spending is: {Housing + Utilities + Groceries + Transportation + Health_Care + Personal_Care + Clothing + Debt}")


"Remaining balance"
print(f"Your remaining balance is: {Income - (Housing + Utilities + Groceries + Transportation + Health_Care + Personal_Care + Clothing + Debt)}")
