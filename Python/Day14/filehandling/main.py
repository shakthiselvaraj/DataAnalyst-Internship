# To Read File

f1 = open('text.txt', 'r')

# Read all text in file

print(f1.read())

# read single line in file

print(f1.readline())

# To Write file

f2 = open('text1.txt', 'w')
f2.write('Hey whatsup!!')

# To read data from one file and write into another file

f3 = open('text3.txt', 'r')
f4 = open('text4.txt', 'w')

for msg in f3:
    f4.write(msg)