total = 0
count = 0

while True:
    number = int(input("Enter a number: "))

    if number < 0:
        break
    total += number
    count += 1

    if count > 0:
        average = total / 2
        print(f"Average of entred number : {average}")
    else:
        print("Positive number")
