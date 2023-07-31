def custom_sort(char):
    if char.islower():
        return (0,char)
    
    elif char.isupper():
        return (1,char)
    
    elif char.isdigit():
        if int(char) %2 !=0:
            return (2,char)
        else:
            return(3,char)
    else:
        return(4,char)

def sort_string(input_string):
    return "".join(sorted(input_string, key=custom_sort))

input_string = "Sorting1234"
print(sort_string(input_string))