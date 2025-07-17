import feedparser
from config import Config


# Collect articles from RSS feeds
def collect_rss_feeds():
    articles = []
    for url in Config.RSS_FEEDS:
        if not url:
            continue
        
        try:
            feed = feedparser.parse(url.strip())
            
            #Vérifie si le flux a été parsé correctement
            if hasattr(feed, 'bozo') and feed.bozo:
                print(f"Warning: Malformed RSS feed for {url}")
            
            for entry in feed.entries:
                try:
                    title = entry.get('title', 'Titre non disponible')
                    link = entry.get('link', '')
                    summary = entry.get('summary', 'Résumé non disponible')
                    published = entry.get('published', '')
                    
                    # Vérifier si le flux a un titre
                    source = 'Source inconnue'
                    if hasattr(feed, 'feed') and hasattr(feed.feed, 'title'):
                        source = feed.feed.title
                    
                    
                    articles.append({
                    'title': title,
                    'url': link,
                    'publication_date': published,
                    'summary': summary,
                    'source': source,
                    
                })
                except Exception as e:
                    print(f"Error when processing an article from {url}: {e}")
                    continue
                
        except Exception as e:
            print(f"Error parsing RSS feed {url}: {e}")
            continue
    return articles
