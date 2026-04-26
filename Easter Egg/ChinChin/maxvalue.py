user_input_one = float(input("Enter first number: "))
user_input_two = float (input("Enter second number: "))


larger_value = max(user_input_one, user_input_two)
smaller_value = min(user_input_one, user_input_two)
sum_value = user_input_one + user_input_two
difference = user_input_one - user_input_two
product = user_input_one * user_input_two
quotent = user_input_one / user_input_two

print("large number is:", larger_value)
print("small number is:", smaller_value)
print("sum = ", sum_value)
print("diffent = ", difference)
print("product = ", product)
print("quotent = ", quotent)
