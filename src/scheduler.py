from src.collectors.rss_collector import collect_rss_feeds
from src.transformers.data_transformer import transform_data
from src.storage.google_sheets_storage import save_to_google_sheets
from config import Config
import time


def run():
    print("Starting the AI watch agent...")
    try:
        while True:
            try:
                articles = collect_rss_feeds()
                if articles:
                    print(f"Collected {len(articles)} articles.")
                    transformed_articles = transform_data(articles)
                    save_to_google_sheets(transformed_articles)
                    print("Successfully saved new articles to Google Sheets.")
                else:
                    print("No new articles found.")
            except KeyboardInterrupt:
                    print("Stop requested by user. Exiting...")
                    break
            except Exception as e:
                print(f"Something went wrong: {e}")                
                
                
            print(f"Waiting {Config.REFRESH_INTERVAL_MINUTES} minutes before the next run...")
            try:
                time.sleep(Config.REFRESH_INTERVAL_MINUTES * 60)
            except KeyboardInterrupt:
                print("\nStop requested by user.")
                break
            
    except KeyboardInterrupt:
        print("\nFinal program termination.")
    except Exception as e:
        print(f"Something went wrong: {e}")