import os


# create folder for store data
# you can use *fname like as *args
def create_folder(*args):
    for fname in args:
        if not os.path.exists(fname):
            os.makedirs(fname)
            yield f'"{fname}" directory created successfully'
        
        
# delete file or folder
def delete_file_folder(fname):
    if os.path.isdir(fname):
        try:
            os.rmdir(fname)
            return 'Directory removed successfully'
        except Exception as e: return e
    elif os.path.isfile(fname):
        os.remove(fname)
        return 'File removed successfully'
    else: return 'File or folder name not found'