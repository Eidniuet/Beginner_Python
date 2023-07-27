def bin_search(l, target, low=None, high=None):
    if low == None:
        low =0

    if high ==None:
        high = len(l)-1

    if high < low :
        return -1
    
    mid = (low + high) //2

    if l[mid]== target:
        return mid
    elif target < l[mid]:
        return bin_search(l, target, low, mid-1 )
    else:
        return bin_search(l, target, mid +1 , high)
    
"""def while_bsearch(l, target):
    min = 0
    max = len(l)-1
    while not max < min:
        mid = (min + max)//2
        if l[mid]== target:
            return mid
        elif target < l[mid]:
            max = mid -1
        else:
            min = mid+1
    return -1"""

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (bin_search(test_list, test_val1))
print (bin_search(test_list, test_val2))