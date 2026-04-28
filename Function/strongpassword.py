def is_strong_password(password):
# 8 characters long
    if len(password) >= 8:
        return True
    else:
        return False

# Testing it
print(is_strong_password("Olasunkanmi"))  
print(is_strong_password("47837"))     
print(is_strong_password("12345678"))  

