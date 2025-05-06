from app import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Song {self.title} by {self.artist}>'
