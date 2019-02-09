import argparse
from .itunescollection import iTunesCollection, iTunesAlbumCollection

def cli():
  parser = argparse.ArgumentParser(prog='itunesdiff', description='Diffs two iTunes XML files.')
  parser.add_argument('xmlfiles', nargs=2,
                      help='Path to two iTunes XML files')
  parser.add_argument('-a', '--albums',action='store_true', help='Diff albums only', default=False)
  args = parser.parse_args()

  if args.albums:
      i1 = iTunesAlbumCollection(args.xmlfiles[0])
      i2 = iTunesAlbumCollection(args.xmlfiles[1])
      i1.diff(i2)
  else:
      i1 = iTunesCollection(args.xmlfiles[0])
      i2 = iTunesCollection(args.xmlfiles[1])
      i1.diff(i2)
