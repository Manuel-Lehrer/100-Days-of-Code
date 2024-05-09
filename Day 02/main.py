print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

total_per_person = (total_bill / number_of_people)*(1+tip_percentage/100)
# Total_per_person_rounded = round(total_per_person, 2)  OPTIONAL
total_per_person_rounded = "{:.2f}".format(total_per_person)

print("Each person should pay: $"+total_per_person_rounded)
# print(f"Each person should pay: $"+{total_per_person_rounded}) OPTIONAL, but must be used if not formatted
