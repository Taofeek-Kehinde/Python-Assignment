'''
START

we are to collect 3 inputs from a user to display sum, average, product, smalles and largest out of all the numbers

END
'''

first_input = int(input("Enter first number "))
second_input = int(input("Enter second number "))
last_input = int(input("Enter last number"))

sum = first_input + second_input + last_input
average = (first_input + second_input + last_input) / 3
product = (first_input * second_input * last_input) 
smallest = min(first_input, second_input, last_input)
largest = max(first_input, second_input, last_input)
print('Sum = ', sum)
print('Average = ', average)
print('Product = ', product)
print('Min = ', smallest)
print('Max = ', largest)
