# valid email conditions:
# username can only contain letters, digits, dashes and underscores
# website name can only have letters and digits
# extension can only contain letters
# max length of the extension is 3

import re # regex

def fun(s):       
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)