import re

for i in range(int(input())):
    try: print(bool(re.compile(input()))) 
    # bool returns the boolean value of the object it passes
    # compile method compiles a regular expression pattern into a regular expression object
    except: print(False)
