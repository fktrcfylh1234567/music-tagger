import sys

from files import tags_from_filename

args = sys.argv[1:]
path = args[0]

underscores = args.count("--underscores") > 0
use_api = args.count("--api") > 0

tags_from_filename(path, underscores=underscores, use_api=use_api)
