import json
import sys
import os

# -------------------------------------------------------------------------------
# 
# Script that makes a config file for each notebook and sends it
# to the published/ tree (using ./inputs/translate.json)
#
# -------------------------------------------------------------------------------

NAME="make_config"  # name of this script

# Get translate.json, to translate HTML file names to branch names
def get_translate():
    with open('./scripts/inputs/translate.json') as f:
        translate = json.load(f)
    return translate

# Get chapter names from translate.json
def get_chapters(translate):
    return translate.values()

# Get config dictionary
# config.userguide_chapter_name : breadcrumb header label
# config.tags.title : META title
# config.tags.meta_description : META description
def get_config(chapter):

    # Shortcut capitalizing first letter of each word except 'and', 'to' 
    def titled(s):
        return s.title().replace('And',"and").replace('To','to')

    # Set base name (without '-')
    base = chapter.replace('-',' ')

    # Exceptions (base name)
    #

    # Set fields
    name = base.capitalize().replace(' tutorial','')
    title = "{} | MATLAB User Guide | plotly".format(titled(base))
    descrip = (
        "A tutorial on how to make beautiful {} "
        "with plotly and MATLAB."
    ).format(base.replace(' tutorial',''))

    # Exceptions (fields)
    if chapter == 'user-guide':
        name = ""
        title = "MATLAB User Guide | plotly"
        descrip = "A User Guide for plotly and its MATLAB API Library"
    if chapter == 'introduction':
        title = "Introduction of Plotly and its MATLAB API Library"
        descrip = "An introduction to plotly and its MATLAB API Library"
    if chapter == 'overview':
        title = "Overview of Plotly and its MATLAB API Library"
        descrip = "An overview of plotly and its MATLAB API Library"
    if chapter == 'streaming-tutorial': 
        name = "Streaming plots"
        title = "Overview of Streaming Plots | MATLAB User Guide | plotly" 
        descrip = (
            "How to graph data in real-time with plotly and MATLAB."
        )

    # Output
    config = dict(
        user_guide_chapter_name=name,
        tags=dict(title=title,meta_description=descrip)
    )

    return config

# Replace config.json 
def replace_config(config, chapter):
    path = os.path.join("./published/includes/", chapter)
    f_config = os.path.join(path,"config.json")
    with open(f_config, "w") as f:
        print "[{}]".format(NAME), '... writes in', f_config
        json.dump(config, f, indent=4)
        f.write("\n")
    return

# -------------------------------------------------------------------------------

def main():

    translate = get_translate()
    chapters = get_chapters(translate)

    for chapter in chapters:
        config = get_config(chapter)
        replace_config(config, chapter)

if __name__ == "__main__":
    main()
