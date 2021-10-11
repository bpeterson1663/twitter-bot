import tweepy

auth = tweepy.OAuthHandler("API_KEY", "API_TOKEN")
auth.set_access_token('ACCESS_TOKEN', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print(user.name)
print(user.followers_count)