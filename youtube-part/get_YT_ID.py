
import googleapiclient.discovery
import pprint as pprint

from dotenv import load_dotenv
import os
import json


def get_YtId(YT_API_KEY, vid_name):
    """Input video name, gets video id. 
    Append id at end of https://www.youtube.com/watch?v= for url
    """
    load_dotenv()

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = YT_API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        order="relevance",
        q=vid_name,
        safeSearch="none"
    )

    response = request.execute()
    return response["items"][0]["id"]["videoId"]


load_dotenv()
yt_ApiKey = os.getenv("YT_API_KEY")
yt_id = get_YtId(yt_ApiKey, "CALMNNESS")

print(f"https://www.youtube.com/watch?v={yt_id}")
