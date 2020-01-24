import eyed3
from eyed3.id3 import frames


def print_tags(filename):
    file = eyed3.load(filename)
    print(file.tag.getTextFrame(frames.ARTIST_FID))
    print(file.tag.getTextFrame(frames.ALBUM_ARTIST_FID))
    print(file.tag.getTextFrame(frames.ALBUM_FID))
    print(file.tag.getTextFrame(frames.TITLE_FID))


def set_tags(filename, title=None, artist=None):
    file = eyed3.load(filename)

    file.tag.title = title
    file.tag.artist = artist
    file.tag.album_artist = artist
    # file.tag.album = u""
    file.tag.save()
