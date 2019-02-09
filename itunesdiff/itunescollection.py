from libpytunes import Library
from collections import OrderedDict

class DiffableCollection:
    def __init__(self, dictionary):
        self.items = dictionary

    def diff(self, other_diffable_collection, sorted_by, named_by):
        removed_keys = set(self.items.keys()) - set(other_diffable_collection.items.keys())
        added_keys = set(other_diffable_collection.items.keys()) - set(self.items.keys())

        def print_differences(prefix, keys, library):
            dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
            diff_items = dictfilt(library.items, keys)
            ordered_diff_items = OrderedDict(sorted(diff_items.iteritems(),
                                                    key=lambda x: sorted_by(x[1])))

            for key in ordered_diff_items:
                print prefix + " " + named_by(ordered_diff_items[key])

        print_differences(">", added_keys, other_diffable_collection)
        print_differences("<", removed_keys, self)


class iTunesCollection(DiffableCollection):
    def __init__(self, path):
        library = Library(path)
        songs = {}
        for id, song in library.songs.items():
            if song:
                songs[(song.artist or "") + song.name] = song
        DiffableCollection.__init__(self, songs)

    def diff(self, other_itunes_collection):
        DiffableCollection.diff(self, other_itunes_collection,
                                lambda x: x.artist,
                                lambda x: x.name + " - " + x.artist)


class iTunesAlbumCollection(DiffableCollection):
    def __init__(self, path):
        library = Library(path)
        albums = {}
        for id, song in library.songs.items():
            if song and song.album:
                albums[song.album + (song.album_artist or "")] = song
        DiffableCollection.__init__(self, albums)

    def diff(self, other_itunes_collection):
        DiffableCollection.diff(self, other_itunes_collection,
                                lambda x: (x.album_artist or "") + x.album,
                                lambda x: x.album + " - " + (x.album_artist or "?"))
