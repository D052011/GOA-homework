day = input("Enter the day of the week: ")

if day == "Monday":
    print("Start of the week")
elif day == "Tuesday" or day == "Wednesday" or day == "Thursday":
    print("Midweek")
elif day == "Friday":
    print("Weekend is near")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Invalid day")