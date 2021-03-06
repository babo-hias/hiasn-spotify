from flask import Flask, request, redirect, g, render_template, session
from spotify_requests import spotify
import os
import startup

app = Flask(__name__)
app.secret_key = 'superduperkey1020'

# ----------------------- AUTH API PROCEDURE -------------------------

@app.route("/auth")
def auth():
    return redirect(spotify.AUTH_URL)


@app.route("/callback/")
def callback():

    auth_token = request.args['code']
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header

    return profile()

def valid_token(resp):
    return resp is not None and not 'error' in resp

# -------------------------- API REQUESTS ----------------------------

@app.route("/")
def index():
    # return render_template('index.html')
    response = startup.getUser()
    return redirect(response)


@app.route('/profile')
def profile():
    if 'auth_header' in session:
        auth_header = session['auth_header']
        # get profile data
        profile_data = spotify.get_users_profile(auth_header)

        # get user playlist data
        playlist_data = spotify.get_users_playlists(auth_header)

        # get user recently played tracks
        recently_played = spotify.get_users_recently_played(auth_header)

        # get user top artists and tracks
        # top_tracks = spotify.get_users_top(auth_header, 'tracks')

        if valid_token(recently_played):
            return render_template("profile.html",
                               user=profile_data,
                               playlists=playlist_data["items"],
                               recently_played=recently_played["items"])

    return render_template('profile.html')


if __name__ == "__main__":
    app.run(port=spotify.PORT)
    # app.run()
    # app.run(host='0.0.0.0', port=spotify.PORT)