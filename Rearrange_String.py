def custom_sort(char):
    if char.islower(): 
        return (0,char) # 0 is order , char is variable
    
    elif char.isupper():
        return (1,char)
    
    elif char.isdigit(): # is digit
        if int(char) %2 !=0: # odd
            return (2,char)
        else: # even
            return(3,char)
    else: # for other char for specified on above
        return(4,char)

def sort_string(input_string):
    return "".join(sorted(input_string, key=custom_sort)) #it will separate as each element in a list after sorted so needed ''.join 

input_string = "Sorting1234"
print(sort_string(input_string))
