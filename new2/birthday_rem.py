bday_file = open('birthday_file.txt')
file = open('birthday_file.txt','r+')
f = file.read()
birthdays = dict(x.split(' ') for x in f.split(','))

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
        bday_info = ','+name+' '+bday
        file.write(bday_info)
        birthdays[name] = bday
        print('Birthday database updated.')
#print(birthdays)
bday_file.close()