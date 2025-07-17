import hashlib
import datetime

def transform_data(articles):
    
    if not articles:
        print("No articles to convert")
        return []
    
    transformed_articles = []
    for article in articles:
        try:
            transformed_articles.append({
            'id': hashlib.sha256(article['url'].encode()).hexdigest(),
            'source': article.get('source', 'Source inconnue'),
            'title': article.get('title', 'itre non disponible'),
            'url': article.get('url', ''),
            'summary': article.get('summary', 'Résumé non disponible'),
            'publication_date': article.get('publication_date', ''),
            'collection_date': datetime.datetime.now().isoformat(),
            'tags': ''
        })
            
        except Exception as e:
            print(f"Error when transforming an article: {e}")
            continue
        
    return transformed_articles