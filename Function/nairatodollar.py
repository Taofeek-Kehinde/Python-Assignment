def dollar_to_naira(dollars):

    if dollars < 0:
        return "Error: Money can't be negative"
    
    rate = 1550
    
 
    naira = dollars * rate
    
    naira = round(naira, 2)
    
    return naira

# Test it
print(dollar_to_naira(10))    
print(dollar_to_naira(5.5))   
print(dollar_to_naira(-2))    
