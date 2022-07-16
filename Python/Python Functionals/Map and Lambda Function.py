# cubic fibonacci sequence

cube = lambda x: x**3 # take x as an argument for the x cube expression

def fibonacci(n):
    fiblist = []
    for i in range(n):
        if len(fiblist) == 0:
            fiblist.append(0)
        elif len(fiblist) == 1:
            fiblist.append(1)
        else:
            fiblist.append(fiblist[i-2]+fiblist[i-1])
    return fiblist

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))) # map takes the fibonacci iterable and maps it w.r.t to the lambda formula given by cube