
for i in range(int(input())):
    a, b = input().split()
    try:
        print(f'{int(a)/int(b):.0f}')
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    #hackerrank requires output for ZeroDivisionError to be "Error Code: integer division or modulo by zero"
    #except (ZeroDivisionError, ValueError) as e:
    #    print("Error Code:", e)
        