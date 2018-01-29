# string = "abc 123,xyz=456"
#dict(x.split(' ') for x in string.split(','))
#{'xyz': '456', 'abc': '123'}'''
bday_file = open('birthdayfile.txt')
#bday_file.close()
birthdays = {}
file = open('birthdayfile.txt','w+')
f = file.read()
print(f)

birthdays = dict(x.split(' ') for x in f.split(','))
'''
for l in f:

    k, v = l.split()
    if k in birthdays:

        birthdays.update({k: v})

    else:

        birthdays[k] = v
'''
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        bday_info = name+' '+bday+','
        #file = open('birthday_file.txt','w+')
        file.write(bday_info)
        #bday_file.close()
        #bday_file = open('birthday_file.txt','r')
        #x = bday_file.read()
        #print(x)
        birthdays[name] = bday
        print('Birthday database updated.')
#print(birthdays)
#x = bday_file.read()
#print(x)

#print(birthdays)
bday_file.close()


