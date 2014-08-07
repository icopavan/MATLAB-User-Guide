from bs4 import BeautifulSoup
import json
import sys

# -------------------------------------------------------------------------------
# 
# Script that converts 
# (using ./inputs/image-map.json)
#
# -------------------------------------------------------------------------------

NAME="image_map"  # file name

# Get input arguments 
def get_args():
    args = sys.argv[1:]
    if not args:
        print ("usage:\n"
               "python {NAME}.py file.html \n"
               "python {NAME}.py file1.html file2.html ...  fileN.html\n".format(NAME=NAME))
        sys.exit(0)
    else:
        return args

# Get HTML soup from HTML file path
def get_soup(file_html):
    with open(file_html, "r") as f:
        print "[{}]".format(NAME), 'Opening', file_html
        return BeautifulSoup(f)

# Get URLs of image maps from image-map.json
def get_imagemap():
    with open("./scripts/inputs/image-map.json") as f:
        imagemap = json.load(f)
    return imagemap.items()[0]

# Replace relative image source to github hosted images in HTML soup
def replace_src(soup, imagemap):
    for img in soup.findAll('img'):
        if img['src'].startswith(imagemap[0]):
            print "[{}]".format(NAME), '... source to translate found:', img['src']
            img['src'] = img['src'].replace(*imagemap)
            print "[{}]".format(NAME), '... source translated to:', img['src']
    return soup

# Replace HTML file 
def replace_file_html(soup, file_html):
    new_html = soup.prettify("utf-8")
    with open(file_html, "wb") as f:
        print "[{}]".format(NAME), '... overwrites', file_html
        f.write(new_html)
        return

# -------------------------------------------------------------------------------

def main():

    files_html = get_args()
    imagemap = get_imagemap()

    for file_html in files_html:
        soup = get_soup(file_html)
        soup = replace_src(soup, imagemap)
        replace_file_html(soup, file_html)


if __name__ == "__main__":
    main()
