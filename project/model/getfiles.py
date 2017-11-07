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

# ===================================================================================
# =============================== FOR TEST PURPOSES =================================
# ===================================================================================

    #fileslist = glob.glob((folder + r'\*.mp3')) #.replace('[','[[]').replace(']','[]]'))              #  normcase(folder + r'\*.mp3'))

def mainbody():
    list = glob.glob(normcase(ini.folder[0]  + r'\*.mp3'))  # )
    for elem in list:
        print(basename(elem))

if __name__ == '__main__':
    #mainbody()
    for dir in ini.folder:
        print('===============================')
        print(dir)
        files = getfileslist(dir)
        for file in files:
            print(file)

