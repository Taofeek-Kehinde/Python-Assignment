number = input("Enter three number: ")

if len(number)==3:
    if number == number[::-1]:
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")
else:
    print("please enter 3 digit number")
