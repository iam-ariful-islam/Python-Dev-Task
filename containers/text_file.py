# create text file with data type
def create_text_file(fname, data):
    with open(fname, 'w') as file:
        if type(data) == dict:
            for i, (k, v) in enumerate(data.items(), start=1):
                file.write(f'{str(i).zfill(2)}. {k} : {v}\n')
        else:
            with open(fname, 'wb') as file:
                file.write(data)
                
# read text file and return data
def read_text_file(fname):
    with open(fname, 'rb') as file:
        return file.read()