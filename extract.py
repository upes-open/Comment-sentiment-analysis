import os
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from util import get_video_id

load_dotenv()
api_key=os.getenv('API_KEY')


# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

def fetch_comments(url):
    video_id = get_video_id(url)
    comments = []
    next_page_token = ''
    while next_page_token is not None:
        results = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=next_page_token,
            maxResults=100
        ).execute()

        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        next_page_token = results.get('nextPageToken')
    
    return pd.DataFrame(comments, columns=['comment'])
