count = 0
for number in range(1, 7):
    for second_number in range(number + 1, 8):
        print(f"{number}, {second_number}", end=" " )
        count +=1

print(f"\nTotal combinations: {count}" )
