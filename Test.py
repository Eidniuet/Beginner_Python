def sum_pyramid(pyramid):
    
    for layer in range(len(pyramid) - 2, -1, -1):
        for pos in range(len(pyramid[layer])):
            if  pyramid[layer][pos] == 0:
                 break
            else:
                pyramid[layer][pos] += max(pyramid[layer + 1][pos], pyramid[layer + 1][pos + 1])
    
    return pyramid[0][0]

pyramid_str = "1 0 0 0\n2 3 0 0\n4 5 6 0\n7 8 9 10"


# line = pyramid_str.split("\n")
# for i in range(len(line)):
#     line[i] = line[i].split(' ')
# output = []
# for i in range(len(line)):
#     current_line = []
#     for j in range(len(line)):
#         if int(line[i][j]) != 0:
#             current_line.append(int(line[i][j])) 
#     output.append(current_line)
# print (output)

lines = pyramid_str.split('\n')
pyramid = []

for line in lines:
    int_list = list(map(int, line.split(' '))) 
    non_zero = [num for num in int_list ] #if num != 0
    pyramid.append(non_zero)

print(pyramid)

# Calculate the sum iteratively
sum_in_pyramid = sum_pyramid(pyramid)
print("Sum of numbers in the pyramid:", sum_in_pyramid)

numberlist = [[1], ["2"], ["3"]]
x = []
for num in numberlist:
    newlist = list(map(str, num))
    x.append(newlist)
print(x)