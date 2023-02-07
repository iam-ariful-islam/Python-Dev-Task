import os
import sys
import subprocess


# create requirements.txt files if not exists
def create_packages_file():
    with open('requirements.txt', 'w') as f:
        lists = ['bs4==0.0.1\n', 'nltk==3.8.1\n', 'scikit-learn==1.2.0\n', 'gensim==4.3.0\n', 'textblob==0.17.1\n', 'xlsxwriter==3.0.2']
        f.writelines(lists)
        f.close()


# install the all needed packages from requirements.txt file
def install_packages():
    # check requirements.txt file exists or not
    if not os.path.exists('requirements.txt'):
        create_packages_file()
        
    package_list = []
    with open('requirements.txt', 'r') as f:
        package_list = f.readlines()
    for package in package_list:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except Exception as e: print(e)