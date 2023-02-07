import os
import sys
import time
import argparse

# import custom modules
from containers.amazon_scraper import AmazonProductInfoScraper
from containers.about import about
from containers.install_packages import install_packages
from containers.files_list import show_files_list
from containers.create_delete_file_folder import create_folder, delete_file_folder
from containers.logs_file import report_info


# read file or program base name
fname = os.path.basename(__file__)

url = 'https://www.amazon.com/dp/B09B9TB61G' # default url
data_folder   = 'data' # default data folder name
output_folder = 'output' # default output folder name
ifile_name = time.strftime('%d.%m.%Y') + '.html' # default input file name
ofile_name = time.strftime('%d.%m.%Y') + '.csv' # default output file name

# custom help message formatter class
class CustomFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                for option_string in action.option_strings:
                    parts.append('%s' % option_string)
            return ', '.join(parts)

# create output file
def action_func(action):
    ext1 = os.path.splitext(ifile_name)[1]
    ext2 = os.path.splitext(ofile_name)[1]
    if ext1=='' or ext2=='':
        report_info('File cannot be found')
        return
    valid = AmazonProductInfoScraper.check_url(url)
    report_info('The url was valid')
    if valid:
        cls_obj = AmazonProductInfoScraper(url)
        if action=='g':
            log = cls_obj.retrieve_webpage()
            report_info(log)
            # cls_obj.print_data() # if you want to print scraping data
            cls_obj.write_webpage_as_file(data_folder+'/'+ifile_name)
        if action=='o':
            cls_obj.read_webpage_from_file(data_folder+'/'+ifile_name)
            cls_obj.convert_data_to_bs4()
            cls_obj.parse_soup_data(output_folder+'/'+ofile_name)
            cls_obj.parse_soup_data(output_folder+'/'+ofile_name)
    
# run the program manually without passing arguments
def manual_mode():
    global url, data_folder, output_folder, ifile_name, ofile_name
    opts = '''
    Program run options:
    ------------------------
    [ 1]. help message        [ 2]. program version    [ 3]. auth info
    [ 4]. packages install    [ 5]. scraping url       [ 6]. create folder
    [ 7]. get scraping data   [ 8]. output file        [ 9]. list of files
    [10]. delete file/folder  _______________________  [00]. quit/close
    '''
    print(opts)
    choice = input('Enter choose your option : ')[0].lower()
    choice_list = ['1', 'h', '2', 'v', '3', 'a', '4', 'p', 'i', '5', 'u', '6', 'f', '7', 'g', '8', 'o', '9', 'l', '10', 'd']
    
    if choice in '0qc':
        print('\nThank you...!!!')
        sys.exit()
        
    while not choice in choice_list:
        choice = input('Wrong choose, enter choose your option again : ')[0].lower()
        if choice in '0qc':
            print('\nThank you...!!!')
            sys.exit()
        
    if choice=='2' or choice=='v': print(f'\n{fname} v1.0')
    elif choice=='3' or choice=='a': about()
    elif choice=='4' or choice=='p' or choice=='i': install_packages()
    elif choice=='5' or choice=='u':
        url = input(f'Enter scraping url(default url: {url}): ') or url
        
    elif choice=='6' or choice=='f':
        data_folder   = input(f'Enter data folder name(default name: "{data_folder}") : ') or data_folder
        output_folder = input(f'Enter output folder name(default name: "{output_folder}") : ') or output_folder
        [report_info(x) for x in create_folder(data_folder, output_folder)]
        
    elif choice=='7' or choice=='g':
        ifile_name = input('Enter scraping data file name: ') or ifile_name
        action_func(action='g')

    elif choice=='8' or choice=='o':
        ofile_name = input('Enter output file name: ') or ofile_name
        action_func(action='o')

    elif choice=='9' or choice=='l': show_files_list()
    elif choice=='10' or choice=='d':
        fn  = input('Enter file or folder name for delete: ')
        report_info(delete_file_folder(fn))
        
    manual_mode()

# run the program by passing the arguments(cli=command-line interface)
def cli_mode(args):
    global url, data_folder, output_folder, ifile_name, ofile_name
    if args.auth: about()
    if args.install: install_packages()
    if args.url: url = args.url
    if args.folder:
        data_folder, output_folder = args.folder[:2] if len(args.folder)>=2 else [args.folder[0], output_folder] if len(args.folder)==1 else [data_folder, output_folder]
        [report_info(x) for x in create_folder(data_folder, output_folder)]
    if args.get:
        ifile_name = args.get
        action_func(action='g')
    if args.output:
        ofile_name = args.output
        action_func(action='o')
    if args.list: show_files_list()
    if args.delete: report_info(delete_file_folder(args.delete))
    

# root function
def main():
    usg_msg = f' python -m {fname} [options...] [arguments...]'
    des_msg = '"Python Dev Task" is python-based web scraping and summarization tool utilizing text paraphrasing'
    log_msg = f'Please, run the program by passing the following arguments. (Exp. python -m {fname} -h)'

    parser = argparse.ArgumentParser(description=des_msg, usage=usg_msg, epilog=log_msg, formatter_class=CustomFormatter)

    parser._optionals.title = 'Optionals arguments'
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0') # read program name with v1.0
    parser.add_argument('-a', '--auth', '--about', action='store_true', help='About of developer information')
    parser.add_argument('-i', '--install', action='store_true', help='Install the all needed packages from file')
    parser.add_argument('-u', '--url', help="Get or scraping information from url")
    parser.add_argument('-f', '--folder', nargs='+', help='Enter folder name to create folder and store data into folder')
    parser.add_argument('-g', '--get', help='Get & store data for output using input url(Exp. *.html/*.txt)')
    parser.add_argument('-o', '--output', help='Create & store data for output file(Exp. *.csv/*.xlsx/*.txt)')
    parser.add_argument('-l', '--list', action='store_true', help='Show the all files list')
    parser.add_argument('-d', '--delete', help='You can delete file or folder')
    
    if len(sys.argv) <= 1: manual_mode()
    else:
        args = parser.parse_args()
        cli_mode(args=args)


# root
if __name__ == '__main__':
    main()