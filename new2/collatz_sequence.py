import sys
def collatz_sequence(num):
    while num!=1:
        if num%2==0:
            num=num//2
        else:
            num=3*num+1
        print(int(num))
        collatz_sequence(num)
    sys.exit()


try:
    print('enter a number:')
    entered_num=int(input())
    collatz_sequence(entered_num)
except ValueError:
    print('valueError:enter number')

