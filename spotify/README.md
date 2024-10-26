This script allows you to do operations with Spotify while e.g.: you are playing a game.
 - Fast-forward music by 30 sec: Right Arrow
 - Rewind music by 30 sec: Left Arrow
 - Next music: Down Arrow
 - Prev music: Up Arrow
 - Stop / Start music: 'Alt' + 'p'
 - You can modify the script so that you can add a song to one of your playlists by pressing a button

To use this script, you have to register your own spotify application.
After that, you'll need to construct a `credentials.yaml` file next to the script containing the following: 
```yaml
client_id: "your app client id"
client_secret: "your app client secret"
```

Install dependencies  
Run the script  
Have fun

([Doc of spotipy functions](https://developer.spotify.com/documentation/web-api/concepts/scopes))
