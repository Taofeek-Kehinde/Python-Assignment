def is_valid_email(email):
#     at least 8 characters long
    if len(email) < 8:
        return False

#     Must contain @ symbol
    if "@" not in email:
        return False

# Cannot start or end with @
    if email[0] == "@":
        return False

    if email[-1] == "@":
        return False

#    If all rules pass, it's valid
    return True

# put to test
print(is_valid_email("Ktaofeek@gmail.com")) 
print(is_valid_email("8 character checked")) 
print(is_valid_email("there should @")) 
print(is_valid_email("should not start wirh @")) 
print(is_valid_email("should not end with @")) 
