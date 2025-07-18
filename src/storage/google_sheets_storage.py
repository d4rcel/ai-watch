import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import Config

def get_google_sheets_client():
    
    print("Connecting to google sheets...")
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(Config.GOOGLE_APPLICATION_CREDENTIALS, scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(Config.SPREADSHEET_KEY).worksheet(Config.GOOGLE_SHEET_NAME)
        print("Inserting in google sheets...")
        return sheet
        
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")
        raise
    


def save_to_google_sheets(articles):
    sheet = get_google_sheets_client()
    header = list(articles[0].keys())
    
    if sheet.row_count == 0:
        sheet.append_row(header)
        
    for article in articles:
        cell = sheet.find(article['id'])
        if cell is None:
            row = [article.get(h, '') for h in header]
            sheet.append_row(row)
