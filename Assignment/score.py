enter_grade = int(input("Enter grade from 0 -100 \n"))

if enter_grade >= 90 or enter_grade == 100:
    print('A') 
elif enter_grade >= 80 or enter_grade == 89:
    print('B')
elif enter_grade >= 70 or enter_grade == 79:
    print('C')
elif enter_grade >= 60 or enter_grade == 69:
    print('D')
else:
    print('F')
