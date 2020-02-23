import sys

from files import tags_from_filename, fill_album_from_tags, print_tags

args = sys.argv[1:]
path = args[0]

if args.count("--print") > 0:
    print_tags(path)
else:
    tags_from_filename(path)
