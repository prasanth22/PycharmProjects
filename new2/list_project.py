def list2string(list):
    str = ''
    i=0
    while i < len(list):
        str = str + list[i]+', '
        i+=1
    return str

spam = ['apples', 'bananas', 'tofu', 'cats']

print(spam)

string = list2string(spam)

print(string)








