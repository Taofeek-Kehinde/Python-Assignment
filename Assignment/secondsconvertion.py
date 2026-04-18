
total_seconds = int(input("Enter number of seconds: "))

hours = total_seconds // 3600          
remaining = total_seconds % 3600
minutes = remaining // 60              
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
