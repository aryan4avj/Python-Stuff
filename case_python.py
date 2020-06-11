def swap_case(s):
    newstring =''
    for a in s: 
# Checking for lowercase letter and converting to uppercase. 
        if (a.isupper()) == True: 
            newstring+=(a.lower()) 
# Checking for uppercase letter and converting to lowercase. 
        elif (a.islower()) == True: 
            newstring+=(a.upper()) 
# Checking for whitespace letter and adding it to the new string as it is. 
        else: 
            newstring+= a
    return newstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
