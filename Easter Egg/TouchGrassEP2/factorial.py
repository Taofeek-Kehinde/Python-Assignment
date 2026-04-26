def factoria(number):
    output = 1
    for result in range(1, number + 1):
        output *= result
        print(output)
    return output

numbers = int(input("Enter a number: "))
print("Factorial is: ", factoria(numbers))
