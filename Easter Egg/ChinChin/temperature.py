temp = float(input("Enter a temperatue: "))

if temp < 0:
    print("Freezing")
elif 0 <= temp <= 15:
    print("Cold")
elif 16 <= temp <= 26:
    print("warm")
else: 
    print("hot")


