import os
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# import custom modules
from containers.gensim_text_summarization import text_summarize
from containers.text_polarity import text_polarity
from containers.html_file import create_html_file, read_html_file
from containers.csv_file import create_csv_file
from containers.xlsx_file import create_xlsx_file
from containers.text_file import create_text_file, read_text_file
from containers.product_info import scrap_product_info



# default file name
file_name = 'data/'+time.strftime('%d.%m.%Y') + '.html'

class AmazonProductInfoScraper:
    __purl  = ''
    __data  = ''
    __soup  = None
    __fname = file_name
    
    # initialize function or constructor method
    def __init__(self, purl):
        self.__purl = purl
        
    # check url is valid or invalid
    # its a class method
    @classmethod
    def check_url(cls, purl):
        try: urlopen(purl)
        except HTTPError as e: return e
        except URLError as e: return 'The server could not be found'
        except Exception as e: return e
        else: return True
        
    # retrieve webpage from url
    def retrieve_webpage(self):
        try: html = urlopen(self.__purl)
        except Exception as e: return e
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                return 'Retrieved data successfully'
                
    # write webpage in a file
    def write_webpage_as_file(self, file_path='', data=''):
        self.__fname = file_path or self.__fname
        ext = os.path.splitext(self.__fname)[1]
        if ext == '.html':
            x = self.__data
            if data: x = data
            create_html_file(self.__fname, x)
        elif ext == '.txt':
            create_text_file(self.__fname, data)
        elif ext == '.xlsx' and type(data)==dict:
            create_xlsx_file(self.__fname, data)
        elif ext == '.csv' and type(data)==dict:
            create_csv_file(self.__fname, data)
                    
    # read webpage data from a file
    def read_webpage_from_file(self, file_path=''):
        self.__fname = file_path or self.__fname
        ext = os.path.splitext(self.__fname)[1]
        if ext == '.html':
            self.__data = read_html_file(self.__fname)
        elif ext == '.txt':
            self.__data = read_text_file(self.__fname)
        
    # print scraping data
    def print_data(self):
        print(self.__data)
        
    # convert webpage data into bs4
    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, 'html.parser')
        
    # parse soup data/scrap data
    def parse_soup_data(self, file_path=''):
        self.__fname = file_path or self.__fname
        fname = os.path.split(self.__fname)[-1]
        fpath = self.__fname
        
        # parse product information
        pinfo = scrap_product_info(self.__soup)
        # add extra with file name
        pname = fpath.replace(fname, 'pinfo_'+fname)
        self.write_webpage_as_file(pname, pinfo)
        
        # parse product features
        features = dict()
        try:
            product_features = self.__soup.find("div", id="feature-bullets").text
            x = [x.strip() for x in product_features.split('\n')[5::]][1]
            x = [x.strip() for x in x.split('  ')]
            for i in range(0, len(x), 2):
                a = [i.strip() for i in x[i].split('-')]
                features[a[0][2:len(a[0])-2:]] = ''.join(a[1:])
            for k, v in features.items():
                ntxt = text_summarize(v)
                txtp = text_polarity(ntxt)
                ftxt = f'Original(Length: {len(v)}, words: {len(v.split())}):\n{v}\n\nGenerated(Length: {len(ntxt)}, words: {len(ntxt.split())}):\n{ntxt}\n{txtp}\n'
                features[k] = ftxt
        except AttributeError: features['N/A'] = 'N/A'
        
        # add extra with file name
        fname = fpath.replace(fname, 'features_'+fname)
        self.write_webpage_as_file(fname, features)
        # set real file path
        self.__fname = self.__fname.replace('features_', '')