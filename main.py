import sys
from os import listdir
from os.path import isfile, join
import re

from tags import set_tags


def files(basepath):
    return [f for f in listdir(basepath) if isfile(join(basepath, f))]


def tags_from_filename(basepath, underscores=False):
    title_regex = "-_(.+)\\."
    artist_regex = "^(.+)_-_"

    for file in files(basepath):
        title = re.findall(title_regex, file)[0]
        artist = re.findall(artist_regex, file)[0]

        if underscores:
            title = title.replace('_', ' ')
            artist = artist.replace('_', ' ')

        print(artist, title)

        filepath = basepath + file
        set_tags(filepath, title=title, artist=artist)


args = sys.argv[1:]
print(args)
path = args[0]

if args.count("--underscores") > 0:
    tags_from_filename(path, underscores=True)
else:
    tags_from_filename(path)
