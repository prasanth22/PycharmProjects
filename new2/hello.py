'''import sys
dir(sys)
s = range(20)
print(s)
b = range(1,10)
print(b)
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
#import shutil,zipfile,logging,webbrowser,requests
import webbrowser
webbrowser.open('http://inventwithpython.com/')
'''
import os
print(os.path.abspath('.')