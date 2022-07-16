
# see zip documentation <https://docs.python.org/2/library/functions.html#zip>

N , X = map(int, input().split())
# N = number of students
# X = number of subjects

# collect list of list of grades for each subject
grades = []
for i in range(X):
    a = list(map(float, input().split()))
    grades.append(a)

studentgrades = zip(*grades)

for e in studentgrades:
    print(f'{sum(e)/X:.1f}')