from fileinput import FileInput
from glob import glob
import os
import shutil
import re

# ATTENTION: there must not be 2 equal key or value
# regex: https://www.w3schools.com/python/python_regex.asp
dict = {
    # search_text : replace_text
    # start
    r'\\'+'"': r'§§§§§§§§',
    # Effect
    r' \[nointeract\]"':          r'" nointeract',
    r' \[withfade\]"':            r'" with fade',
    r' \[withdissolve\]"':        r'" with dissolve',
    r' \[withslowdissolve\]"':    r'" with slowdissolve',
    r' \[withhpunch\]"':          r'" with hpunch',
    r' \[withflash\]"':           r'" with flash',
    r' \[withvpunch\]"':          r'" with vpunch',
    r' \[withDissolve20\]"':      r'" with Dissolve(2.0)',
    r'msgid "\[nvl_clear\]"':     r'    # nvl clear',
    r'msgstr "\[nvl_clear\]"':    r'    nvl clear',
    # first
    r'msgid "(.*?) \[special_delimiter\] (.*?)"':       r'    # "\1" "\2"',
    r'msgstr "(.*?) \[special_delimiter\] (.*?)"':      r'    "\1" "\2"',
    r'msgstr "\[(.*?)\] (.*?)"':                        r'    \1 "\2"',
    r':\nmsgid "(.*?)"':                                r':\n    # "\1"',
    r'    # (.*?)\nmsgstr "(.*?)"':                     r'    # \1\n    "\2"',
    # after
    # r'# (.*?) "(.*?)"': r'msgid "[\1] \2"',
    r'    # "\[(.*?)\] (.*?)"':         r'    # \1 "\2"',
    # Comment
    # r':\n\nmsgid': r':\nmsgid',
    # r'rpy:(.*?)\ntranslate': r'rpy:\1 #-#-# translate',
    # r'strings:\n\n# ': r'strings: #|#|# # ',
    # r'\ntranslate': r'\n#§translate',
    # r'updated at (.*?)-(.*?)-(.*?) (.*?):(.*?)\n\n# ': r'updated at \1-\2-\3 \4:\5 #|#|# # ',
    # end
    # r'    #':                   r'#',
    # r'    old "(.*?)"':         r'msgid "\1"',
    # r'    new "(.*?)"':         r'msgstr "\1"',
    r'§§§§§§§§': r'\\'+'"',
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # c = re.compile(search_text)

    # Replace the target string
    # filedata = filedata.replace(search_text, replace_text)
    filedata = re.sub(search_text, replace_text, filedata)
    # TODO: to improve

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}):
    newpathFile = fileRename(pathFile, extension=".rpy")
    print(pathFile)
    for search_text in dict.keys():
        replacetext(pathFile=newpathFile, search_text=search_text,
                    replace_text=dict[search_text])


def getListFiles(extension):
    # Get the list of all files and directories
    path = "game/tl/"
    dir_list = glob(path + "/**/*"+extension, recursive=True)
    return dir_list


def potorpy():
    for path in getListFiles(extension=".po"):
        replaceDictionary(path, dict=dict)


def fileRename(pathFile, extension):
    pre, ext = os.path.splitext(pathFile)
    shutil.copyfile(pathFile, pre + extension)
    return pre + extension


potorpy()
