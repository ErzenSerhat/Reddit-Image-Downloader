import praw

# Reddit API kimlik bilgileri
reddit_client_id = "#"
reddit_client_secret = "#"
reddit_username = "#"
reddit_password = "#"


# Reddit API'ye bağlanma
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent="Reddit Image Downloader")

# İndirilecek subreddit ve post sayısı
subreddit_name = "gamermemes"
post_limit = 30

# Reddit'ten görselleri indirme
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.hot(limit=post_limit)

image_urls = []
for post in posts:
    if post.url.endswith((".jpg", ".jpeg", ".png")):
        image_urls.append(post.url)

# Indirilen görselleri linkleme
print(image_urls)
