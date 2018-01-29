from urllib import request
url = 'http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'

def file(pdf_url):
    response = request.urlopen(pdf_url)
    data = response.read()
    data_str = str(data)
    lines = data_str.split("\\n")
    dest = r'data.csv'
    fx = open(dest,"w")
    for line in lines:
        fx.write(line + "\n")

    fx.close()

file(url)
