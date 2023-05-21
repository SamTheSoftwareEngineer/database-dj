"""Models for Playlist app."""
"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                         primary_key=True, 
                         autoincrement=True)

    name = db.Column(db.String(30), 
                         nullable=False)
    
    description = db.Column(db.String(50), 
                         nullable=False)
    playlist = db.relationship('PlaylistSong')

class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                         primary_key=True, 
                         autoincrement=True)

    title = db.Column(db.String(50), 
                         nullable=False)
    
    artist = db.Column(db.String(50), 
                         nullable=False)
    song = db.relationship('PlaylistSong', backref='songs')



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlistsongs"

    id = db.Column(db.Integer,
                         primary_key=True, 
                         autoincrement=True)

    playlist_id = db.Column(db.Integer,
                                db.ForeignKey("playlists.id", ondelete="CASCADE"))
    
    song_id = db.Column(db.Integer,
                                db.ForeignKey("songs.id", ondelete="CASCADE"))
    playlist_song = db.relationship('Playlist', backref='playlistsongs')
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)