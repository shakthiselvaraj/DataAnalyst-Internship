import csv

with open('ex1.csv', 'w') as c:

    a = csv.writer(c)
    a.writerow(['school', 'student'])
    a.writerow(['ABCD', 'aiai'])
