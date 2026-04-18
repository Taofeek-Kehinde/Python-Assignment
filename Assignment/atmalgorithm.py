'''
START
1.  when customer inserts card
2. Read card data to identify account
3. Prompt customer to enter PIN
4. Verify PIN against bank records
5. If PIN is incorrect, allow 2 more attempts, then retain card and end
6. If PIN is correct, prompt customer to select transaction type
7. Customer selects "Withdraw Cash"
8. Prompt customer to enter withdrawal amount
9. Check if requested amount is available in ATM
10. Check if customer’s account balance is sufficient
11. Check if amount follows ATM rules: multiples of available bills, under daily limit
12. If all checks pass, then:  
    a. Deduct amount from account balance  
    b. Dispense cash  
    c. Print receipt if requested  
    d. Eject card  
13. If any check fails, then:  
    a. Display error message explaining why  
    b. Eject card without dispensing cash
END
'''
