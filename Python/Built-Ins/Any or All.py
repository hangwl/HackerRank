# any() returns True if any element in the iterable is true
# all() returns True if all elements in the iterable is true

# Condition 1: All integer in list are positive
# Condition 2: Any one integer is a palindrome

N, integers = int(input()), list(map(int, input().split()))
print('True' if all(i > 0 for i in integers) and any(str(i)==str(i)[::-1] for i in integers) else 'False')