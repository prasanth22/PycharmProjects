import re
import glob, os

test =''' 15JF1A0522 RT31051 COMPILER DESIGN 30 49 3
15JF1A0522 RT31052 DATA COMMUNICATION 28 26 3
15JF1A0522 RT31053 PRINCIPLES OF PROGRAMMING LANGUAGES 29 41 3
15JF1A0522 RT31054 DATABASE MANAGEMENT SYSTEMS 28 44 3
15JF1A0522 RT31055 OPERATING SYSTEMS 25 26 3
15JF1A0522 RT31056 COMPILER DESIGN LAB 24 50 2
15JF1A0522 RT31057 OPERATING SYSTEM & LINUX PROGRAMMING LAB 25 50 2
15JF1A0522 RT31058 DATABASE MANAGEMENT SYSTEMS LAB 24 42 2
15JF1A0522 RT31059 SEMINAR 48 0 1
'''
'''for i in range(0,len(test)):
    mark = re.compile(r'\d\d')
    mo = mark.search(test)

print( mo.group())
'''
atRegex = re.compile(r'\w+')
print(atRegex.findall(test))
data = test.split()
print(data)
lis1 = [int(s) for s in re.findall(r'\b\d\d\b',test )]
print(lis1)
total = sum(lis1)
print(total)
'''
lis2 = [for s in re.findall(r'\d\d\w\w\d\w\d\d\d',test )]
print(lis2)
'''
'''
os.chdir("C:\sample\python")
for file in glob.glob("*.py"):
    print(file)

NameMarks = 
15JF1A0522 RT31051 COMPILER DESIGN 30 49 3
15JF1A0522 RT31052 DATA COMMUNICATION 28 26 3
15JF1A0522 RT31053 PRINCIPLES OF PROGRAMMING LANGUAGES 29 41 3
15JF1A0522 RT31054 DATABASE MANAGEMENT SYSTEMS 28 44 3
15JF1A0522 RT31055 OPERATING SYSTEMS 25 26 3
15JF1A0522 RT31056 COMPILER DESIGN LAB 24 50 2
15JF1A0522 RT31057 OPERATING SYSTEM & LINUX PROGRAMMING LAB 25 50 2
15JF1A0522 RT31058 DATABASE MANAGEMENT SYSTEMS LAB 24 42 2
15JF1A0522 RT31059 SEMINAR 48 0 1

marks =re.findall(r'\b\d\d\b',NameMarks)
nameSub = re.findall(r'\D[A-Z]* \D[A-Z]*',NameMarks)
print(nameSub)
subjects = [nameSub[0],nameSub[1],nameSub[2]+nameSub[3],nameSub[4],nameSub[5],nameSub[6],nameSub[7]+nameSub[8]+nameSub[9],nameSub[10]+nameSub[11]]
print(subjects)

a=[' COMPILER DESIGN', ' DATA COMMUNICATION', ' PRINCIPLES OF PROGRAMMING LANGUAGES', ' DATABASE MANAGEMENT SYSTEM', ' OPERATING SYSTEMS', ' COMPILER DESIGN LAB', ' OPERATING SYSTEM & LINUX PROGRAMMING LAB', ' DATABASE MANAGEMENT SYSTEMS LAB','SEMINOR']
print(a)

my_marks = {}

x = 0

for sub in nameSub:
    my_marks[sub] = marks[x]
    x+=1

print(my_marks)
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
'''