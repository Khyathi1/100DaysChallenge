print("Welcome to tip calculator")
bill = float(input("What is your Total Bill : "))
tip = int(input("How much tip(percentage) would you like to give [10%, 12% , 15%] : "))
split = int(input("How many people to split the bill : "))

total =(bill + (bill*tip/100))/split
print("Each person should pay : ",round(total,2))