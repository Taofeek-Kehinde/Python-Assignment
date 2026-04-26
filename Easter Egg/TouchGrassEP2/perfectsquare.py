def is_perfect_square(number):
    if number < 0:
        return False

        square = int(number ** 0.5)
        return square * square == number


num = int(input("Enter a number: "))
print(is_perfect_square(num))
