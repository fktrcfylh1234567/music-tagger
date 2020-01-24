from os import listdir
from os.path import isfile, join
import re

from api import get_album
from tags import set_tags


def files(basepath):
    return [f for f in listdir(basepath) if isfile(join(basepath, f))]


def tags_from_filename(basepath, underscores=False, use_api=False):
    title_regex = "-_(.+)\\."
    artist_regex = "^(.+)_-_"

    for file in files(basepath):
        filepath = basepath + file
        title = re.findall(title_regex, file)[0]
        artist = re.findall(artist_regex, file)[0]

        if underscores:
            title = title.replace('_', ' ')
            artist = artist.replace('_', ' ')

        if use_api:
            album = get_album(artist, title)
            if album:
                print(artist, title, album)
                set_tags(filepath, title=title, artist=artist, album=album)
            else:
                print(artist, title)
                set_tags(filepath, title=title, artist=artist)

        else:
            print(artist, title)
            set_tags(filepath, title=title, artist=artist)

        print('-------------------------------------')
