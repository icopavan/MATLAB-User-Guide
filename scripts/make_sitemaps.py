import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that makes a django sitemaps file containing all the user guide items
# (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="make_sitemaps"  # name of this script

# Get translate.json, to translate HTML file names to branch names
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get chapter names from translate.json
def get_chapters(translate):
    return translate.values()

# Get sitemaps items
# N.B. To be imported in 
def get_items(chapters):
    locations = []
    lmfiles = []
    for chapter in chapters:
        locations += ["'/matlab/{}/'".format(chapter)]
        lmfiles += [("os.path.join("
            "settings.TOP_DIR,"
            "'shelly',"
            "'templates',"
            "'api_docs',"
            "'includes',"
            "'user_guide',"
            "'matlab',"
            "'{}',"
            "'body.html')"
        ).format(chapter)]
    return locations, lmfiles

# Generate python_sitemaps.py file
# See streambed/api_docs/ for more info
def get_sitemaps_py(locations, lmfiles):
    sitemaps_py = (
        "from django.conf import settings\n"
        "import os\n\n"
        "def items():\n"
        "    items = [\n"
    )
    for location, lmfile in zip(locations,lmfiles):
        sitemaps_py += (
        "        dict(\n"
        "            location={location},\n"
        "            lmfile={lmfile},\n"
        "            priority=0.5\n"
        "        )"
        ).format(location=location,lmfile=lmfile)
        if location != locations[-1]:
            sitemaps_py += ",\n"
    sitemaps_py += (
        "\n    ]"
        "\n    return items"
        "\n"
    )
    return sitemaps_py

# Replace matlab_sitemaps.py
def replace_sitemaps(sitemaps_py):
    f_urls = "./published/matlab_sitemaps.py"
    with open(f_urls, "w") as f:
        print "[{}]".format(NAME), '... writes in', f_urls
        f.write(sitemaps_py)
    return

# -------------------------------------------------------------------------------

def main():

    translate = get_translate()
    chapters = get_chapters(translate)

    locations, lmfiles = get_items(chapters)
    sitemaps_py = get_sitemaps_py(locations, lmfiles)

    replace_sitemaps(sitemaps_py)


if __name__ == "__main__":
    main()
