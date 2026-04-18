'''
START
The condition is too loop between 0-9 
there is row and colum it's to range between 0-9 and 
 IF 
print < lessthan if the condition true which means if row modulus 2 => remainder 2 is equal to 1 print less then else => if the condition is not true print > greaterthan and end in single qoute'

END

'''
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
        print()
