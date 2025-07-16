import feedparser
from config import Config


# Collect articles from RSS feeds
def collect_rss_feeds():
    articles = []
    for url in Config.RSS_FEEDS:
        if not url:
            continue
        feed = feedparser.parse(url.strip())
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'url': entry.link,
                'publication_date': entry.get('published', ''),
                'summary': entry.summary,
                'source': feed.feed.title,
                
            })
    return articles
