print("welcome to the tip calculator.")
a = float(input("What's your bill? $" ))
b = int(input("what percentage would you like to give? 10,12 or 15?"))
c = int(input("How many people to split the bill?"))
tip = (b/100)*a
people = (tip +a)/c
print(f"Each person should pay: ${round(people, 2)}")