# x = 3
# y = 39
# d = 4

# def divisible(x,y,d):
#     res = []
#     for i in range(x, y):
#         if i % d == 0:
#             res.append(i)
#     return len(res)
# a = divisible(x,y,d)
# print (a)

# string = 'AXRAIL PTE LTD'
# output = '5432ECBA'

# def reverse (string):
#     return string[::-1]
# x = reverse(string)
# print (x)

def solution(x):
    stack = []
    x = list(x)
    for i in range(len(x)):
        if stack and stack[-1] == x[i]:
            stack.pop()
        else:
            stack.append(x[i])
    return "".join(stack)
# x = "XZZXXYYZ"
# x2 = 'XYZYYZYX'
# x3 = 'YXYXYX'
# y = solution(x)
# y2 = solution(x2)
# y3 = solution(x3)
# print(y)
# print(y2)
# print(y3)
x = 'XYZYYZYXZXYZZXYYX'
y = solution(x)
print(y)



