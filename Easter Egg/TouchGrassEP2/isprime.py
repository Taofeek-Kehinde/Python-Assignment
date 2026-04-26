def is_prime(number):
    if number < 2:
        return False
    for num in range(2, int(number ** 0.5) +1):
        if number % num == 0:
            return False

    return True

user_input = int(input("Enter a number: "))
print(is_prime(user_input))
