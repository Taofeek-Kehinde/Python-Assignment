power = int(input("Enter N: "))

print("Powers of 1:", end=" ")
for number in range(1, power + 1):
    print(1 ** number, end=" ")

print("\nPowers of 2:", end=" ")
for number in range(1, power + 1):
    print(2 ** number, end=" ")

print(f"\nPowers of {power}:", end=" ")
for number in range(1, power + 1):
    print(power ** number, end=" ")
