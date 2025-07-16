import hashlib
import datetime

def transform_data(articles):
    print("Transforming data :::")
    transformed_articles = []
    for article in articles:
        transformed_articles.append({
            'id': hashlib.sha256(article['url'].encode()).hexdigest(),
            'source': article['source'],
            'title': article['title'],
            'url': article['url'],
            'summary': article['summary'],
            'publication_date': article['publication_date'],
            'collection_date': datetime.datetime.now().isoformat(),
            'tags': ''
        })
        
    return transformed_articles