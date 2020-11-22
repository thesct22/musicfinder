from flask import Flask
from flask import jsonify
import soundcloud
import spotify_artist
import spotify_playlist
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return "hello there"

@app.route('/soundcloud/recent')
def scr():
   return jsonify(soundcloud.getrecent())

@app.route('/soundcloud/popular')
def scp():
   return jsonify(soundcloud.gethots())
   
@app.route('/spotify/artists/recent')
def sfar():
   return jsonify(spotify_artist.getrecent())
   
@app.route('/spotify/artists/popular')
def sfap():
   return jsonify(spotify_artist.gethots())

@app.route('/spotify/playlists/recent')
def sfpr():
   return jsonify(spotify_playlist.getrecent())
   
@app.route('/spotify/playlists/popular')
def sfpp():
   return jsonify(spotify_playlist.gethots())

if __name__ == '__main__':
   app.run(host ='0.0.0.0', port = 5000, debug = True)