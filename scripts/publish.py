from bs4 import BeautifulSoup
import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that 
# 
# (-) parses HTML files leaving only <body></body> template
# (-) strips <h1> tag (i.e. the NB's title)
# (-) strips <style></style> inside body
# (-) strips <script></script> inside body (which inserts MathJax)
# (-) strips last <pre><pre> inside body (which inserts CSS into NB)
#
# (*)  adds this template to the published/ tree (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="publish"  # name of this script

# Get input arguments 
def get_args():
    path = sys.argv[0]
    args = sys.argv[1:]
    if not args:
        print ("usage:\n"
               "python {NAME}.py file.html \n"
               "python {NAME}.py file1.html file2.html ...  fileN.html\n".format(NAME=NAME))
        sys.exit(0)
    else:
        return args, path

# Get HTML soup from HTML file path
def get_soup(file_html):
    with open(file_html, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_html
        return BeautifulSoup(f)

# Get HTML <body> 
def get_body(soup):
    print "[{}]".format(NAME), '... grabs <body>'
    return soup.body

# Strip title (i.e. the first h1) tag from body
def strip_title(body):
    H1 = body.findAll('h1')
    H1[0].extract()
    print "[{}]".format(NAME), '... strip first <h1> title'
    return body

# Strip style tag from body
def strip_style(body):
    body.style.extract()
    print "[{}]".format(NAME), '... strip <style>'
    return body

# Strip script tag from body
def strip_script(body):
    body.script.extract()
    print "[{}]".format(NAME), '... strip <script> (which inserts MathJax)'
    return body

# Strip last pre tag from body
def strip_last_pre(body):
    Pre = body.findAll('pre')
    Pre[-1].extract()
    for div in body.findAll('div')[::-1]:
        if all(i in div['class'] for i in ['cell','border-box-sizing','code_cell','rendered']):
            div.extract()
            break
    print "[{}]".format(NAME), '... strip last <pre> and parent <div> (which inserts CSS into NB)'
    return body

## (*)

# Get translate.json, to translate HTML file names to branch names
# (e.g. s00_homepage/s00_homepage.html to home)
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get the directory tree for body.html leaf
def get_tree(file_html, translate):
    branch="published/includes/"
    file_html_base = os.path.basename(file_html)
    for old, leaf in translate.items():
        old_base = os.path.basename(old).replace('.ipynb','.html')
        if old_base == file_html_base:
            return "{branch}{leaf}/".format(branch=branch,leaf=leaf)
    else:
        print "[{}]".format(NAME), '!!! URL tail not found in translate.json'

# Make directory tree
def make_tree(tree):
    if not os.path.exists(tree):
        print "[{}]".format(NAME), '... making', tree
        os.makedirs(tree)
    else:
        print "[{}]".format(NAME), '...', tree, 'already exists OK'

# Replace body.html templates
def replace_templates(body, tree):
    f_body = os.path.join(tree, "body.html")
    with open(f_body, "wb") as f:
        print "[{}]".format(NAME), '... writes in', f_body
        body = body.prettify().encode('utf8')
         body = body.replace('<body>','')
         body = body.replace('</body>','')
        f.write(str(body))
    return

# -------------------------------------------------------------------------------

def main():

    files_html, path = get_args()
    translate = get_translate()

    for file_html in files_html:
        soup = get_soup(file_html)
  
        body = get_body(soup) 

        body = strip_title(body)
        body = strip_style(body)
        body = strip_script(body)
        body = strip_last_pre(body)

        tree = get_tree(file_html, translate)
        make_tree(tree)
        replace_templates(body, tree)

if __name__ == "__main__":
    main()
