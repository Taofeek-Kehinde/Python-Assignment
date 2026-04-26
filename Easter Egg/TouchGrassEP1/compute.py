total = 0

for number in range(1,100,2):
    print(number)
    total += number / (number + 3)

print(f"Sum = {total}")
