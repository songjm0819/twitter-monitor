import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime

query = "생리대 lang:ko"

tweets = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= 200:
        break

    tweets.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "text": tweet.content,
        "user": tweet.user.username,
        "created": tweet.date
    })

df = pd.DataFrame(tweets)
df.to_csv("tweets.csv", index=False, encoding="utf-8-sig")

print("done")
