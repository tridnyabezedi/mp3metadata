icon_path_main = r'D:\CodeProjects\PyCharm\mp3metadata\ico' \
                 r'ns\11949967862046187178kid3.svg.med.png'
icon_path_folder = r'D:\CodeProjects\PyCharm\mp3metadata\ico' \
                   r'ns\folder-icon.png'
# ui_path = r'D:\CodeProjects\Qt\mp3ui\mainwindow.ui'
# ui_path = r'D:\CodeProjects\PyCharm\mp3metadata\ui\mp3ui\mainwindow.ui'
# ui_path_py = r'D:\CodeProjects\PyCharm\mp3metadata\ui\mp3ui\mainwindow.py'
ui_path = r'\ui\mp3ui\mainwindow.ui'
ui_path_py = r'\ui\mp3ui\mainwindow.py'
# /re/:\D[\w]+(\s*[\w]+)*
# /re/:[^\d\s][\w]+(\s*[\w()]+)*
# /re/:[^\d\s][\w()]+(\s*[\w()]+)*

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
