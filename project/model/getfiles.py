from ..presenter import ini
import glob
from os.path import normcase, basename
import os
import fnmatch

def getfileslist(folder):
    fileslist = os.scandir(folder)
    fileslist = [folder + os.sep + x.name for x in fileslist
                 if fnmatch.fnmatch(x.name, '*.mp3')]
    return fileslist