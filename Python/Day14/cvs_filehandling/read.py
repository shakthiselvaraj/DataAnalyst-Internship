import csv

with open('ex.csv', 'r') as c:
    a = csv.reader(c, delimiter = '\t')
    next(a)
    for line in a:
        print(line)

