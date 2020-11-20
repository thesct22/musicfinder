from flask import Flask
import soundcloud
import spotify_artist
import spotify_playlist

app = Flask(__name__)

@app.route('/soundcloud/recent')
def scr():
   return soundcloud.getrecent()

@app.route('/soundcloud/popular')
def scp():
   return soundcloud.gethots()
   
@app.route('/spotify/artists/recent')
def sfar():
   return spotify_artist.getrecent()
   
@app.route('/spotify/artists/popular')
def sfap():
   return spotify_artist.gethots()

@app.route('/spotify/playlist/recent')
def sfpr():
   return spotify_playlist.getrecent()
   
@app.route('/spotify/playlist/popular')
def sfpp():
   return spotify_playlist.gethots()

if __name__ == '__main__':
   app.run()