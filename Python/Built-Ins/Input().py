# sample input

# space separated integers x and k
# 1 4

# str function of x
# x**3 + x**2 + x + 1

# we can use the map() function to assign respective inputs to x and k
# then use eval() to parse the expression in the second input line

x, k = map(int, input().split())
print('True' if eval(input()) == k else 'False')
