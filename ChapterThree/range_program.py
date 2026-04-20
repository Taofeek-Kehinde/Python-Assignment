'''
START

The question was what is this code does 
when i ran it shows < less than if row remainder 2 is 1 
else it print > greaterthan if it's not 
it is a condition to check if < modulus 2 is 1 in 0-9 or > in 0 to 9 and a end
to make it single row instead of column

END
'''
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
print()
