
user_input = int(input("Enter N: "))

total = 0

for number in range(1, user_input + 1):
    total +=number

print(f"Sum of first {number} numbers: {total}")
