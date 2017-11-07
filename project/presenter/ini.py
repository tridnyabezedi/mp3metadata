from mutagen import id3
import pathlib

icon_path_main = str(pathlib.PurePath('.', 'project', 'view', 'icons',
                                      '11949967862046187178kid3.svg.med.png'))
icon_path_folder = str(pathlib.PurePath('.', 'project', 'view', 'icons', 'folder-icon.png'))
ui_path_ui = str(pathlib.PurePath('.', 'project', 'view', 'ui', 'mp3ui', 'mainwindow.ui'))
uiorpy = True # True = ui, False = pypython3

vocabulary = {
    'title':        ('TIT2', id3.TIT2),
    'album':        ('TALB', id3.TALB),
    'tracknum':     ('TRCK', id3.TRCK),
    'artist':       ('TPE1', id3.TPE1),
    'author':       ('TPE2', id3.TPE2),
    'disk':         ('TPOS', id3.TPOS),
    'year':         ('TDRC', id3.TDRC),
    'genre':        ('TCON', id3.TCON),
    'comment':      ('COMM', id3.COMM),
    'encode':       ('TENC', id3.TENC),
    'authority':    ('TCOP', id3.TCOP)
}

tablegraphs = (('artist', 'album', 'year', 'genre', 'tracknum', 'title'),   # Graphs order
    ('Filename', 'Artist', 'Album', 'Year', 'Genre', '#',       'Title'),   # Graphs names
    (150,       120,       120,     50,     90,      40,         200))      # TableView columns width (

