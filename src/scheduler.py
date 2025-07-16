from collectors.rss_collector import collect_rss_feeds
from transformers.data_transformer import transform_data

def app():
    print("Starting the AI watch agent...")
    # while True:
    #     articles = collect_rss_feeds()
    #     if articles:
    #         transformed_articles = transform_data(articles)
    #         break


if __name__ == "__main__":
    app()