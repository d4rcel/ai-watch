import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_APPLICATION_CREDENTIALS, SPREADSHEET_KEY, GOOGLE_SHEET_NAME

def get_google_sheets_client():
    
    print("Connecting to google sheets...")
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_APPLICATION_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SPREADSHEET_KEY).worksheet(GOOGLE_SHEET_NAME)
    return sheet


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