'''
START
we are to do the factorial of 5 number which make the result 120
END
'''
number = 5
count = 1
factoria = 1

while count <= number:
    factoria *=count
    count += 1

print(f"factoria of {number} is {factoria}")
