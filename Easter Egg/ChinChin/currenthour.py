hour = int(input("Enter current hou 0-23 "))
if 5 <= hour  <= 11:
    print("Good Morning")
elif 12 <= hour <=17:
    print("Good Afternoon")
elif 18 <= hour <= 22:
    print("Good Night")
else:
    print("Coding Time")
