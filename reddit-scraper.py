import praw
import pandas as pd
from datetime import datetime
import re

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

subreddit = reddit.subreddit('subreddit_name')

data = {
    'title': [],
    'score': [],
    'url': [],
    'num_comments': [],
    'created': [],
    'author': [],
    'selftext': [],
    'flair': []
}

for submission in subreddit.hot(limit=50):
    data['title'].append(submission.title)
    data['score'].append(submission.score)
    data['url'].append(submission.url)
    data['num_comments'].append(submission.num_comments)
    data['created'].append(datetime.fromtimestamp(submission.created))
    data['author'].append(submission.author.name if submission.author else 'N/A')
    data['selftext'].append(re.sub('\s+', ' ', submission.selftext.strip()))
    data['flair'].append(submission.link_flair_text)

df = pd.DataFrame(data)
df.to_csv('reddit_scraper_output.csv', index=False)

top_post = subreddit.top(limit=1)
for submission in top_post:
    print(f"Top post of all time:\nTitle: {submission.title}\nScore: {submission.score}\nLink: {submission.url}\n")
