from mutagen import id3
from .getfiles import getfileslist
from os.path import basename
import re
from ..presenter import ini

class Song:
    vocabulary = ini.vocabulary

    def __init__(self, path):
        self.__id3tag = self.__getid3(path)
        self.path = path
        self.filename = basename(path)

    def __getid3(self, path_):
        try:
            return id3.ID3(path_)
        except:
            return {}

    def __getitem__(self, item):
        try:
            return str(self.__id3tag[self.vocabulary[item][0]])
        except:
            return ''

    def __str__(self):
        tempstr = ''
        for key in self.__id3tag:
            if key != r'APIC:':
                tempstr += '        {}: {}\n'.format(key, self.__id3tag[key])
        return 'Filename: {0}\n' \
               'Tags:\n{2}'.format(self.filename, self.path, tempstr)

    def change_tags(self, dict_):
        def getvalue(tag_value):
            if tag_value[1]:
                return re.search(tag_value[0], self.filename).group()
            else:
                return tag_value[0]
        for word in self.vocabulary:
            try:
                self.__id3tag[self.vocabulary[word][0]] = self.vocabulary[word][1]\
                    (text=getvalue(dict_[word]))
            except:
                pass

    def save_changes(self):
        self.__id3tag.save()

class SongList:
    def __init__(self, path_to_folder):
        # fileslist = getfileslist(os.path.normcase(workdir_))
        fileslist = getfileslist(path_to_folder)
        self.__songlist = [Song(path) for path in fileslist]
        self.path = path_to_folder

    def __call__(self, *args, **kwargs):
        return self.__songlist

    def __str__(self):
        return str(self())

    def __getitem__(self, item):
        return self.__songlist[item]

    def song(self, songnum):
        if songnum <= len(self.__songlist):
            return self.__songlist[songnum]
        else:
            raise IndexError

    def print(self, full=0, pic=False):
        print('Folder: {}'.format(self.path))
        for song in self.__songlist:
            if full == 1:
                print(song[1].keys())
                for tag in song[1]:
                    if pic or tag != r'APIC:':
                        print('    {} {}'.format(tag, song[1][tag]))
            elif full == 2:
                try:
                    song[1].pop(r'APIC:')
                except:
                    pass
                print(song[1])
            elif full == 3:
                print (song)
            print()

    def change_tags_for_all(self, dict_):
        for song in self.__songlist:
            song.change_tags(dict_)
            song.save_changes()

    def save_all(self):
        for song in self.__songlist:
            song.save_changes()

    # def gettag(self, row_, tagname):
    #     try:
    #         return str(self.__songlist[row_][1][self.vocabulary[tagname][0]])
    #     except:
    #         return ''

def mainbody():
    fileslist = getfileslist(ini.folder[0])
    songlist = SongList(fileslist)
    songlist.changetags(ini.tagdict)
    songlist.save()

def testbody():
    fileslist = ini.folder[2]
    songlist = SongList(fileslist)
    # songlist.print()
    #songlist.changetags(ini.tagdict)
    # songlist.print(full=3)
    print(songlist)
    for i in songlist:
        print(i['tracknum'])
    for word in ini.vocabulary:
        print(word)
    print(ini.vocabulary['title'][0])
    for i in songlist:
        print(i['title'])
    #songlist.save()
    # print()
    #print(songlist[0][0])
    #print(songlist[0][1])
    # print(ini.artist)
    # print(ini.album)
    # match = re.search(ini.tracknum, songlist[3][0])
    # print(match.group())
    # print(re.search(ini.tracknum, songlist[0][0]).group())
    # print(re.search(ini.title, songlist[0][0]).group())
    # print(re.search(ini.tagdict['tracknum'][0], songlist[0][0]).group())
    # print(re.search(ini.tagdict['title'][0], songlist[0][0]).group())
    #print(songlist.createtable())
    # print(songlist[6][1])

def anothertestbody():
    fileslist = getfileslist(ini.folder[1])
    # print(fileslist)

    # songlist = SongList(fileslist)
   # [[print(xx) for xx in x] for x in songlist.createtable()]
    #[print(x) for x in songlist.createtable()]
    # songlist.print(full=True)
    #for tag in songlist[0][1]:
        #print (tag, songlist[0][1][tag])
    #print(songlist[1][1])
    # songlist.print(full=2)
    # for word in songlist.fary:
    #     print(word, songlist.gettag(1, word))

if __name__ == '__main__':
    #anothertestbody()
    testbody()
