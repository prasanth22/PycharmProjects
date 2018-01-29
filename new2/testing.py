import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(res.text[:250])
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(1000000):
    playFile.write(chunk)
playFile.close()