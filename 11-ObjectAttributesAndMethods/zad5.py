class Music():
    def __init__(self,performer,song,album,year):
        self.performer = performer
        self.song = song
        self.album = album 
        self.year = year

    def __str__(self):
        return f"Performer: {self.performer} \nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"
       


m = Music("Ed Sheeran", "Hearts Don't","Divide", 2017)
print(m)


f = Music("Ed ", "Heon't","Die", 2077)
print(f)
        
d = Music("Edzzzz ", "Heozzzzn't","Diez", 20887)
print(d)