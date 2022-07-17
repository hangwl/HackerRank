import re

# A group() expression returns one or more subgroups of the match.
# x.group(0) returns the entire match
# x.group(1) returns the first parenthesized subgroup

# A groups() expression returns a tuple containing all the subgroups of the match.

# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name. <subgroup name>

condition = r"([a-zA-Z0-9])\1+"

m = re.search(condition, input())

if m:
    print(m.group(1))
else:
    print(-1)