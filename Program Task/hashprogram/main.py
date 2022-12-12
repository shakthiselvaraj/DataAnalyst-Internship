""" Given an integer,N, and N space-separated integers as input,
create a tuple,t , of those N integers. Then compute and print the result of hash(t)."""

N = int(input('Enter no of integer in tuples:'))
n = map(int, input().split())
t = tuple(n)
print(hash(t))
