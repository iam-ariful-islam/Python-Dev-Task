import os


# show all files list of current directory
def show_files_list():
    # get current working directory
    c_dir = os.getcwd()
    infos = os.listdir(c_dir)

    fd, fl = [], []
    for x in infos:
        if os.path.isfile(x): fl.append(x)
        elif os.path.isdir(x): fd.append(x)

    # full directory path
    print('* Full Path :', c_dir)
    print('* Directory :', os.path.split(c_dir)[-1]+'/', end='\n\n')
    
    # print only files list
    for n, f in enumerate(fl, start=1):
        print(f'{str(n).zfill(2)}. {f}')
        
    print() # print new line
    
    # print /directory files list
    for n, d in enumerate(fd, start=1):
        print(f'{str(n).zfill(2)}. {d}/')
        for c, f in enumerate(os.listdir(c_dir+'/'+d), start=1):
            print(f'\t{str(c).zfill(2)}. {f}')