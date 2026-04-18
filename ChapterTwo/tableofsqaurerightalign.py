'''

START

the task is to calculate the sqaure and cubes of the numbers from 0.5 

AND

print out the result in table format and use escape sequence to achieve the colum
BUT
will be right align

'''

print("number  square  cube")

for number in range(6):
    square = number **2
    cube = number **3

    print(f"{number:<7} {square:<7} {cube}")
