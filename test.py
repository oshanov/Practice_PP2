class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs =[]
    def song_add(self,song):
        self.songs.append(song)
        print(f'{song} added')
    def song_del(self,song):
        if song in self.songs:
            self.songs.remove(song)
        print(f'{song} deleted')
    def show(self):
        print(f'Playlist {self.name}:')
        for i in self.songs:
            print(i)

myplay = Playlist('Sleep')
myplay.song_add('Not Like Us')
myplay.song_add('GIRL LIKE ME')
myplay.show()
del Playlist.show
