from mutagen import id3
from getfiles import getfileslist
from os.path import basename
import re
import ini


class SongList:
    vocabulary = {
        'title':       ('TIT2',         id3.TIT2),
        'album':       ('TALB',         id3.TALB),
        'tracknum':    ('TRCK',         id3.TRCK),
        'artist':      ('TPE1',         id3.TPE1),
        'author':      ('TPE2',         id3.TPE2),
        'disk':        ('TPOS',         id3.TPOS),
        'year':        ('TDRC',         id3.TDRC),
        'genre':       ('TCON',         id3.TCON),
        'comment':     ('COMM',         id3.COMM),    # 'COMM::eng'
        # ('url', 'WXXX', id3.WXXX),
        'encode':      ('TENC',         id3.TENC),
        'authority':   ('TCOP',         id3.TCOP)
    }

    tablegraphs = ('artist', 'album', 'year', 'genre', 'tracknum', 'title')

    def __init__(self, fileslist):
        self.list_ = [[basename(path), self.__getid3(path)] for path in fileslist]

    def __getid3(self, path_):
        try:
            return id3.ID3(path_)
        except:
            return {}

    def __str__(self):
        pass

    def __getitem__(self, item):
        return self.list_[item]

    def print(self, full=0, pic=False):
        for song in self.list_:
            print(song[0])
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
            print()

    def __getvalue(self, tag_value, path):
        if tag_value[1]:
            return re.search(tag_value[0], path).group()
        else:
            return tag_value[0]

    def changetagsforall(self, dict_):
        for song in self.list_:
            for word in self.vocabulary:
                try:
                    song[1][self.vocabulary[word][0]] = self.vocabulary[word][1]\
                        (text=self.__getvalue(dict_[word], song[0]))
                except:
                    pass

    def changetags(self, songnum, dict_):
        song_ = self.list_[songnum]
        for word in self.vocabulary:
            try:
                song_[1][self.vocabulary[word][0]] = self.vocabulary[word][1]\
                    (text=self.__getvalue(dict_[word], song_[0]))
            except:
                pass

    def saveall(self):
        for song in self.list_:
            song[1].save()

    def save(self, songnum):
        self.list_[songnum][1].save()

    def __checkforvalue(self, song_, word_):
        try:
            return str(song_[word_])
        except:
            return ''

    def createtable(self):
        table = [[song[0]] +
                 [self.__checkforvalue(song[1], self.vocabulary[word][0])
                  for word in self.tablegraphs]
                 for song in self.list_]
        return table

    def gettag(self, row_, tagname):
        try:
            return str(self.list_[row_][1][self.vocabulary[tagname][0]])
        except:
            return ''


def mainbody():
    fileslist = getfileslist(ini.folder[0])
    songlist = SongList(fileslist)
    songlist.changetags(ini.tagdict)
    songlist.save()


def testbody():
    fileslist = getfileslist(ini.folder[9])
    songlist = SongList(fileslist)
    # songlist.print()
    songlist.changetags(ini.tagdict)
    songlist.print(full=True)
    songlist.save()
    # print()
    #print(songlist[0][0])
    #print(songlist[0][1])
    # print(ini.artist)
    # print(ini.album)
    # match = re.search(ini.tracknum, songlist[3][0])
    # print(match.group())
    print(re.search(ini.tracknum, songlist[0][0]).group())
    print(re.search(ini.title, songlist[0][0]).group())
    print(re.search(ini.tagdict['tracknum'][0], songlist[0][0]).group())
    print(re.search(ini.tagdict['title'][0], songlist[0][0]).group())
    #print(songlist.createtable())
    # print(songlist[6][1])


def anothertestbody():
    fileslist = getfileslist(ini.folder[7])
    print(fileslist)
    songlist = SongList(fileslist)
   # [[print(xx) for xx in x] for x in songlist.createtable()]
    #[print(x) for x in songlist.createtable()]
    # songlist.print(full=True)
    #for tag in songlist[0][1]:
        #print (tag, songlist[0][1][tag])
    #print(songlist[1][1])
    songlist.print(full=2)
    # for word in songlist.vocabulary:
    #     print(word, songlist.gettag(1, word))

if __name__ == '__main__':
    anothertestbody()
    #testbody()
