from src.collectors.rss_collector import collect_rss_feeds
from src.transformers.data_transformer import transform_data
from src.storage.google_sheets_storage import save_to_google_sheets

def run():
    print("Starting the AI watch agent...")
    articles = collect_rss_feeds()
    if articles:
        print(f"Collected {len(articles)} articles.")
        transformed_articles = transform_data(articles)
        save_to_google_sheets(transformed_articles)
        print("Successfully saved new articles to Google Sheets.")
    else:
        print("No new articles found.")
    print("AI watch agent finished.")
