# Python Dev Task

### **A Python-based Web Scraping and Summarization Tool Utilizing Text Paraphrasing.**

that can be used to quickly extract, paraphrase and summarize information from a variety of websites for a variety of use cases.

<br/>

## Task Description

A project to build a Python-based web scraping and summarization tool that utilizes text
paraphrasing. The tool will take a target website URL as _input()_ and then extract relevant
information from the website using web scraping techniques. The extracted text will then be
paraphrased using natural language processing and machine learning algorithms, to generate a
summary of the main ideas presented on the website. The summary will be presented in a
concise and coherent manner.

## Task Requirments
this project is developed using all new os, software and tools.

* **Operating System :** Windows10/11, Kali Linux2022.4
* **Software :** Python3.10, Visual Studio Code

<table><tr><td>

| Package Name | Version |
| --- | --- |
| bs4 | == 0.0.1 |
| textblob | == 0.17.1 |

</td><td>

| Package Name | Version |
| --- | --- |
| nltk | == 3.8.1 |
| gensim | == 4.3.0 |

</td></tr> </table>


## Installation

First [Download](https://www.python.org/downloads/), install and configure [Python](https://www.python.org/doc/). Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install on.

* Windows installation
* Kali linux installation
* Mac installation

---
### Use [sudo](https://www.kali.org/docs/general-use/sudo/) and [pip](https://www.kali.org/docs/general-use/sudo/) or [pip3](https://www.kali.org/docs/general-use/sudo/) for installing packages.
1. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) or [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) for web scraping. [Note: Using it, errors may occur because it is not a browser].
2. [NLTK](https://www.nltk.org/install.html) or Natural language processing toolkit for process language.
3. [Sklearn](https://scikit-learn.org/stable/install.html) or scikit-learn for machine learning.
4. [Gensim](https://radimrehurek.com/gensim/auto_examples/index.html#documentation) for text summarisation.
5. [Textblob](https://textblob.readthedocs.io/en/dev/) for text processing and polarity of text.
6. [CSV](https://docs.python.org/3/library/csv.html) for create csv file.
7. [xlsxwriter](https://xlsxwriter.readthedocs.io/getting_started.html) for create xlsx file.

```bash
# install package using below command(method #1)
pip3 install bs4
pip3 install nltk
pip3 install scikit-learn
pip3 install gensim
pip3 install textblob
pip3 install xlsxwriter

# one line command (method #2)
pip3 install bs4 nltk scikit-learn gensim textblob xlsxwriter
```
### **or**
```bash
# install package using below command
sudo pip install bs4 nltk scikit-learn gensim textblob xlsxwriter
```

## Notes
The `requirements.txt` file, lists of all the Python libraries that my "**_Python Dev Task_**" depends on and installs those packages from the file:

```
pip install -r requirements.txt
```

### **or**

```
sudo pip install -r requirements.txt
```

## CLI Options

```bash
python -m main.py --help <press-enter>
```

```
usage:  python -m main.py [options...] [arguments...]

"Python Dev Task" is python-based web scraping and summarization tool utilizing text paraphrasing

Optionals arguments:
  -h, --help           show this help message and exit
  -v, --version        show program's version number and exit
  -a, --auth, --about  About of developer information
  -i, --install        Install the all needed packages from file
  -u, --url            Get or scraping information from url
  -f, --folder         Enter folder name to create folder and store data into folder
  -g, --get            Get & store data for output using input url(Exp. *.html/*.txt)
  -o, --output         Create & store data for output file(Exp. *.csv/*.xlsx/*.txt)
  -l, --list           Show the all files list
  -d, --delete         You can delete file or folder

Please, run the program by passing the following arguments. (Exp. python -m main.py -h)
  ```
### **or**

## Menual Options

```bash
python -m main.py <press-enter>
```

```
    Program run options:
    ------------------------
    [ 1]. help message        [ 2]. program version    [ 3]. auth info
    [ 4]. packages install    [ 5]. scraping url       [ 6]. create folder
    [ 7]. get scraping data   [ 8]. output file        [ 9]. list of files
    [10]. delete file/folder  _______________________  [00]. quit/close

Enter choose your option : 
  ```

## Usages

```bash
# use cli-options
python -m main.py -u <url> -f <in_foldername> <out_foldername> -g <scrap_filename.html/*.txt> -o <out_filename.txt/*.csv/*.xlsx>
```

## Remember
* Manually run the program, please maintain the serial by enter your choice- (1-10) or (h, v, a, p, i, u, f, g, o, l, d), (0, q, c for quit/close the program).
* Run the program on cli-options, show the help message.
* If any errors or actions occur then it will be saved to the **_log/errors.log_** file.
* Default folders name: data, output, log. [Note: You can change the folders name by input].
* Default files name: *.html, *.csv. [Note: You can change the files name by input].
* The urls that have been worked with. see the **_urls.txt_** file.

## Contributing

[<img alt="me" width="40px" style="border-radius: 50%;" src="images/me.jpeg" />](https://jonakisoft.net/iam_ariful_islam.php) **Md. Ariful Islam** <br/>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## For more or connect with me

[<img alt="github" width="45px" src="images/github.png" />](https://github.com/iam-ariful-islam)
[<img alt="twitter" width="45px" src="images/twitter.png" />](https://twitter.com/am_ariful_islam)

## License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)
