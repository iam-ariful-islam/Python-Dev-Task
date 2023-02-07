# create html file to store scraping data
def create_html_file(fname, data):
    try:
        file = open(fname, 'wb')
        file.write(data.encode())
        file.close()
    except Exception as e: print(e)
    
    
# read scraping data from html file
def read_html_file(fname):
    data = ''
    try:
        with open(fname) as file:
            data = file.read()
    except Exception as e: print(e)
    return data