"""Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple."""


from collections import namedtuple
N = int(input())
entry = namedtuple('entry', ','.join(input().split()))
print(f'{sum([int(entry(*input().split()).MARKS) for i in range(N)])/N:.2f}')