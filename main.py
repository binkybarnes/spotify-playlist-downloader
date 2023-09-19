import json
from dotenv import load_dotenv
import os
import base64
from requests import post
from requests import get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def get_playlist_songnames(token, playlist_id):
    url = "https://api.spotify.com/v1/playlists/"
    headers = get_auth_header(token)

    query_url = url + playlist_id
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    return json_result


token = get_token()
json_result = get_playlist_songnames(token, "2ol0oRkvlgpGo4BIewZ7e2")

file = open("output.json", "w")
file.write(json.dumps(json_result, indent=2))
file.close()
