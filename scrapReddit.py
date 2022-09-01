import enum
from pydoc import cli
import urllib.request, json, time


wsbUrl = 'https://api.pushshift.io/reddit/search/submission/?subreddit=wallstreetbets&sort=desc&sort_type=created_utc'
cursorUTC = round(time.time())
cursorInterval = 600


allPosts = []

for i in range(10):
    cursorUrl = wsbUrl + f'before={cursorUTC}'
    cursorUTC -= cursorInterval
    with urllib.request.urlopen(cursorUrl) as url:
        posts = json.loads(url.read().decode())['data']
        allPosts += [post for post in posts if 'removed_by_category' not in post]


res = []
[res.append(x) for x in allPosts if x['id'] not in [i['id'] for i in res]]
