from mutagen import id3
import pathlib

icon_path_main = str(pathlib.PurePath('.', 'icons',
                                      '11949967862046187178kid3.svg.med.png'))
icon_path_folder = str(pathlib.PurePath('.', 'icons', 'folder-icon.png'))
ui_path_ui = str(pathlib.PurePath('.', '.', 'ui', 'mp3ui', 'mainwindow.ui'))
# ui_path_ui = '.' + os.sep + 'ui' + os.sep + 'mp3ui'+ os.sep +'mainwindow.ui' # r'.\ui\mp3ui\mainwindow.ui'
ui_path_py = r'.\ui\mp3ui\mainwindow.py'
uiorpy = False # True = ui, False = pypython3
vocabulary = {
    'title':        ('TIT2', id3.TIT2),
    'album':        ('TALB', id3.TALB),
    'tracknum':     ('TRCK', id3.TRCK),
    'artist':       ('TPE1', id3.TPE1),
    'author':       ('TPE2', id3.TPE2),
    'disk':         ('TPOS', id3.TPOS),
    'year':         ('TDRC', id3.TDRC),
    'genre':        ('TCON', id3.TCON),
    'comment':      ('COMM', id3.COMM),  # 'COMM::eng'
    # ('url', 'WXXX', id3.WXXX),
    'encode':       ('TENC', id3.TENC),
    'authority':    ('TCOP', id3.TCOP)
}

tablegraphs = (('artist', 'album', 'year', 'genre', 'tracknum', 'title'),   # Graphs order
    ('Filename', 'Artist', 'Album', 'Year', 'Genre', '#',       'Title'),   # Graphs names
    (150,       120,       120,     50,     90,      40,         200))      # TableView columns width (


# if uiorpy:
#     ui_path = ui_path_ui
# else:
#     ui_path = ui_path_py
# /re/:\D[\w]+(\s*[\w]+)*
# /re/:[^\d\s][\w]+(\s*[\w()]+)*
# /re/:[^\d\s][\w()]+(\s*[\w()]+)*
# ui_path = r'D:\CodeProjects\Qt\mp3ui\mainwindow.ui'
# ui_path = r'D:\CodeProjects\PyCharm\mp3metadata\ui\mp3ui\mainwindow.ui'
# ui_path_py = r'D:\CodeProjects\PyCharm\mp3metadata\ui\mp3ui\mainwindow.py'

# ===================================================================================
# =============================== FOR TEST PURPOSES =================================
# ===================================================================================
link1 = r'D:\CodeProjects\PyCharm\mp3me' \
        r'tadata\nothing_going_on.mp3'
link2 = r'D:\CodeProjects\PyCharm\mp3metadata\01. Flowers In Fire.mp3'
link3 = r'D:\Music\Sevval Sam\test\Şevval Sam - Karadeniz (2008)' \
        r'\01 - Hey Gidi Karadeniz - копия.mp3'

folder1 = r'D:\Music\_test\Şevval Sam - Karadeniz (2008)'
# folder = r'D:\Music\Sevval Sam\test\Şevval Sam - Karadeniz (2008)'
folder2 = r'D:\Music\_test\Bei Bei and Shawn Lee - Into the Wind (2010) -V0-'
folder3 = r'D:\Music\_test\2'
folder4 = r'D:\Python'
folder = [folder1, folder2, folder3, folder4,
          r'D:\Music\!{ew10}',                                  # 4
          r'D:\Music\[K-pop]\Melon Chart 04.03.15 TOP 100',     # 5
          r'D:\Music\_test\Имаго',                              # 6
          r'D:\CodeProjects\PyCharm\mp3metadata',               # 7
          r'D:\Music\_test\2011 - Vampires On Tomato Juice',    # 8
          r'D:\Music\_test\]]][[['                              # 9
          ]

artist = 'Şevval Sam'
album = 'Karadeniz'
year = 2008
tracknum = r'\d*'
title = r'[A-Za-z]+(\s*[A-Za-z]+)*'  # (?=\s|\.)'

tagdict = {
    'artist': ['Şevval Sam', False],
    'album': ['Karadeniz', False],
    'year': ['2008', False],
    'tracknum': [r'\d*', True],
    'title': [r'[A-Za-z]+(\s*[A-Za-z]+)*', True],
    'disk': ['', False],
    'genre': ['Turkish Folk', False]
}

if __name__ == '__main__':
    print(tagdict['album'])
    print(tagdict.keys())
    print(tablegraphs[2])
    print(ui_path_ui)
