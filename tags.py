import eyed3
from eyed3.id3 import frames


def print_tags(filename):
    file = eyed3.load(filename)
    artist = file.tag.getTextFrame(frames.ARTIST_FID)
    album_artist = file.tag.getTextFrame(frames.ALBUM_ARTIST_FID)
    title = file.tag.getTextFrame(frames.TITLE_FID)
    album = file.tag.getTextFrame(frames.ALBUM_FID)
    print(artist, '-', title)


def get_tags(filename):
    file = eyed3.load(filename)
    artist = file.tag.getTextFrame(frames.ARTIST_FID)
    title = file.tag.getTextFrame(frames.TITLE_FID)
    return artist, title


def set_tags(filename, title=None, artist=None, album=None, release_date=None):
    file = eyed3.load(filename)

    if title:
        file.tag.title = title

    if artist:
        file.tag.artist = artist
        file.tag.album_artist = artist

    if album:
        file.tag.album = album

    if release_date:
        file.tag.original_release_date = release_date
        file.tag.release_date = release_date

    file.tag.save()
