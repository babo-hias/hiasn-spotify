from flask_spotify_auth import getAuth, refreshAuth, getToken

# Add your client ID
CLIENT = json.load(open('conf.json', 'r+'))
# CLIENT_ID = CLIENT['id']
CLIENT_ID = os.environ["CLIENT_ID"]

# aDD YOUR CLIENT SECRET FROM SPOTIFY
# CLIENT_SECRET = CLIENT['secret']
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

# Callback and port
PORT = "8081"
# CALLBACK_URL = "http://127.0.0.1"
CALLBACK_URL = "https://www.hiasn-music-dash.heroku.com"

# Add needed scope from spotify user
SCOPE = "playlist-modify-public playlist-modify-private user-read-recently-played user-top-read"

# token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown 
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)


def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))


def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()


def getAccessToken():
    return TOKEN_DATA