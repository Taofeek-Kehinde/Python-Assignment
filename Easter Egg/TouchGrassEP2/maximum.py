def maximum(first_number, second_number):
    if first_number > second_number:
        return first_number
    else:
        return second_number

number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
print("Maximum = ", maximum(number_one, number_two))        
