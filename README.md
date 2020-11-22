Particulars:

Flask app that finds the recently tweeted Soundcloud songs, Spotify artists and playlists

Install with pip:

```sh
pip install -r requirements.txt
```

File structure:

    .gitignore
    Dockerfile
    ignrtis.py
    lab.py
    main.py
    nginx.conf
    Procfile
    requirements.txt
    sample1.txt
    soundcloud.py
    spotify_artist.py
    spotify_playlist.py
    start.sh
    tree.txt
    uwsgi.ini
    
No subfolders exist 

for production mode run 
```sh
start.sh
```

for debug mode run 
```shell
python main.py
```
Docker image availbale on [Docker Hub](https://hub.docker.com/repository/docker/thesct22/musicfinder-backend)

running on [Heroku](http://dry-citadel-29832.herokuapp.com)

endpoints:
    * /soundcloud/recent
    * /soundcloud/popular
    * /spotify/artists/recent
    * /spotify/artists/popular
    * /spotify/playlists/recent
    * /spotify/playlists/popular
