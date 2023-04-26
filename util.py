from urllib.parse import urlparse, parse_qs
def get_video_id(url):
    """
    Extracts the video ID from a YouTube video URL
    """
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    elif query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        elif query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # if the URL is not recognized as a YouTube video URL
    raise ValueError('Invalid YouTube URL')
