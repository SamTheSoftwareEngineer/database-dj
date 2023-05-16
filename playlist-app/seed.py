from app import db
from models import Song, Playlist, PlaylistSong

db.drop_all()
db.create_all()

"""Sample data for playlist app."""


song1=Song(title='Kuzu kuzu', artist='Tarkan')
song2=Song(title='All I want for christmas is you', artist='Mariah Carey')
song3=Song(title='Dudu Dudu', artist='Tarkan')
song4=Song(title='Dom dom kursunu', artist='Ibolipa')
song5=Song(title='Watermelon Sugar', artist='Harry Styles')
song6=Song(title='Staying Alive', artist='Bee Gees')
song7=Song(title='I Will Survive', artist='Gloria Gaynor')
song8=Song(title='Blurred Lines', artist='Robin Thicke & Pharrell Williams')
song9=Song(title='New York, New York', artist='Frank Sinatra')

list1 = Playlist(name='Turkish', description='Turkish pop')
list2 = Playlist(name='US 50', description='Trending Pop')
list3 = Playlist(name='Oldiez', description='60s to 90s')


ps1 = PlaylistSong(playlist_id ='1', song_id='1')
ps2 = PlaylistSong(playlist_id ='1', song_id='3')
ps3 = PlaylistSong(playlist_id ='1', song_id='4')
ps4 = PlaylistSong(playlist_id ='2', song_id='2')
ps5 = PlaylistSong(playlist_id ='2', song_id='4')
ps6 = PlaylistSong(playlist_id ='2', song_id='5')
ps7 = PlaylistSong(playlist_id ='3', song_id='6')
ps8 = PlaylistSong(playlist_id ='3', song_id='7')
ps9 = PlaylistSong(playlist_id ='3', song_id='9')
ps10 = PlaylistSong(playlist_id ='2', song_id='8')

