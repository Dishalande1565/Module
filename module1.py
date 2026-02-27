# string=input("enter string:")
# print(type(string))
# print(string)

# string=input('enter string:')
# print(len(string))

#wap to check length of given string.
#if length is more than 8 then its valid string otherwise it is invalid.

# string=input('enter string:')

# if len(string)>=8:
#     print('valid string')
# else:
#     print('invalid string')

string=input('enter string:')

# if len(string)<=8 or " " in string:
#     print('Invalid string')
# else:
#     print('valid string')

# if len(string)>=8 and " " not in string and string.isdigit():
#     print('Valid string')
# else:
#     print('Invalid string')

# if len(string)>=8 and " " not in string and any(ch.isdigit() for ch in string) and any(string.isupper() for ch in string) and any(ch in '!@#$%^&*~' for ch in string ):
#     print('Valid string')
# else:
#     print('Invalid string')

def Pass_validation(password):

    if len(password) < 8:
        return f"Your password len is {len(password)} and required is greater than 7"
    
    if " " in password:
        return "Remove white spaces in your password"
    
    if not any(ch.isdigit() for ch in string):
        return "Add atleast 1 digit in your password"
    
    if not any(ch.isupper() for ch in string):
        return "No upper case letter"
    
    if not any(ch.lower() for ch in string):
        return "No lower case letter"
    
    if not any(ch in "~!@#$%^&*" for ch in string):
        return 'No special symbol present'
    
    else:
        return 'password is valid'
    
res=Pass_validation("pythonprog123$")
print(res)
res2=Pass_validation("pythonProgra")
print(res2)


