import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

days = calendar.monthrange(year, month)
print(f"Days in month: {days}")
