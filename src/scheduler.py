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
                print(f"Erreur inattendue dans la boucle principale: {e}")
                print("Le processus va continuer malgré cette erreur...")
                
                
                
            print(f"Waiting {Config.REFRESH_INTERVAL_MINUTES} minutes before the next run...")
            try:
                time.sleep(Config.REFRESH_INTERVAL_MINUTES * 60)
            except KeyboardInterrupt:
                print("\nArrêt demandé par l'utilisateur.")
                break
            
    except KeyboardInterrupt:
        print("\nArrêt définitif du programme.")
    except Exception as e:
        print(f"Erreur critique qui force l'arrêt du programme: {e}")