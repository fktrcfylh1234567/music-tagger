import re
from os import listdir
from os.path import isfile, join

import tags
from api import get_album


def files(basepath):
    return [f for f in listdir(basepath) if isfile(join(basepath, f))]


def print_tags(basepath):
    for file in files(basepath):
        filepath = basepath + file

        try:
            tags.print_tags(filepath)
        except AttributeError:
            pass


def tags_from_filename(basepath):
    title_regex = "-_(.+)\\."
    artist_regex = "^(.+)_-_"

    renamed = 0
    skipped = 0

    for file in files(basepath):
        filepath = basepath + file
        title_re = re.findall(title_regex, file)
        artist_re = re.findall(artist_regex, file)

        if len(title_re) == 0 or len(artist_re) == 0:
            skipped += 1
            continue

        title = title_re[0].replace('_', ' ')
        artist = artist_re[0].replace('_', ' ')

        try:
            tags.set_tags(filepath, title=title, artist=artist)
            renamed += 1
        except BaseException:
            skipped += 1

    print('renamed', renamed, 'skipped', skipped)


def fill_album_from_tags(basepath):
    for file in files(basepath):
        filepath = basepath + file
        artist, title = tags.get_tags(filepath)
        album = get_album(artist, title)

        if album:
            print(artist, title, album)
            tags.set_tags(filepath, album=album)
