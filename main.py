from dotenv import load_dotenv
import os
from requests import get
import json

load_dotenv()

song_name = "DRIP TOO HARD (Remix)"


def get_auth_header(access_token):
    return {
        "Authorization": "Bearer " + token,
        "Accept": "applicaiton/json"
    }


def get_video_id(token, vid_name):
    url = "https://youtube.googleapis.com/youtube/v3/search"
    headers = get_auth_header(token)

    query = f"?part=snippet&maxResults=1&order=relevance&q={vid_name}&safeSearch=none&key={token}"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    return json_result


token = os.getenv("YT_API_KEY")

print(get_video_id(token, song_name))
