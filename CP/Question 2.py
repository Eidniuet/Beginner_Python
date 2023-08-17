def twoSum(arr, S):
    res = []
    numset = set()
    for i in range(len(arr)-1,0,-1):
        diff = S - arr[i]
        if diff in numset:
            res.append([diff, arr[i]])
        numset.add(arr[i])
    return res

def main ():
	nums = [3, 5, 2, 2, -4, 8, 11]
	S = 7
	print(twoSum(nums, S))
main()