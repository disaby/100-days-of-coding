# Day 2 Project. Tip Calculator
# - get the total bill
# - choose tip % (10, 12, 15)
# - number of people should pay

total=float(input("Enter the total bill: "))
tip=int(input("Enter the tip percentage (10, 12, 15): "))
n_people=int(input("Number of people: "))
correct_t=False

while not correct_t:
    match tip:
        case 10:
            break
        case 12:
            break
        case 15:
            break
        case _:
            tip=input(f"Not available tip perc. ({tip}). Re-enter: ")
            tip=int(tip)
            
calc=(total*tip/100)/n_people
calc="{:.2f}".format(round(calc,2))  #float round to 2 decimals pyhon (stackoverflow)

print(f"\n#Each person should pay {calc} $")
        