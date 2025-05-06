from flask import request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from app import app, db
from models import Song
import os

@app.route('/api/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    return jsonify([{
        'id': s.id,
        'title': s.title,
        'artist': s.artist,
        'duration': s.duration,
        'filename': s.filename
    } for s in songs])

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

@app.route('/api/songs', methods=['POST'])
def upload_song():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'File missing'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Extract metadata using Mutagen
    try:
        audio = MP3(file_path, ID3=EasyID3)
        duration = audio.info.length  # Duration in seconds (float)
        title = audio.get('title', [filename])[0]  # Fallback to filename
        artist = audio.get('artist', ['Unknown Artist'])[0]
    except Exception as e:
        # Fallback if metadata extraction fails
        title = os.path.splitext(filename)[0]  # Use filename as title
        artist = 'Unknown Artist'
        duration = 0.0

    # Convert duration to "MM:SS" format (e.g., 125.5 → "2:05")
    minutes, seconds = divmod(int(duration), 60)
    formatted_duration = f"{minutes}:{seconds:02d}"

    # Save to database
    new_song = Song(
        title=title,
        artist=artist,
        duration=formatted_duration,
        filename=filename
    )
    db.session.add(new_song)
    db.session.commit()

    return jsonify({'message': 'Song uploaded successfully'}), 201

@app.route('/music/<filename>')
def serve_music(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    songs = Song.query.all()
    return render_template('player/upload.html', songs=songs)
  # only upload.html because template_folder is already set
