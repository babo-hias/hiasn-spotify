from flask_spotify_auth import getAuth, refreshAuth, getToken

PORT = "8081"

# LOCAL
# CLIENT = json.load(open('conf.json', 'r+'))
# CLIENT_ID = CLIENT['id']
# CLIENT_SECRET = CLIENT['secret']
# CALLBACK_URL = "http://127.0.0.1"

# HEROKU
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
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