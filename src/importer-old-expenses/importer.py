from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from filters import apply_all_filters
try:
    from config import SPREADSHEET_ID, GOOGLE_CREDENTIALS
except ModuleNotFoundError:
    SPREADSHEET_ID = "fallback_spreadsheet_id"
    GOOGLE_CREDENTIALS = {"fallback": "credentials"}


def initialize_api_client():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_info(
        GOOGLE_CREDENTIALS, scopes=scopes)
    service = build('sheets', 'v4', credentials=credentials)
    return service


def get_spreadsheet_data(service):
    spreadsheet_id = SPREADSHEET_ID
    range_name = 'Sheet1!A1:F42'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    filtered_values = apply_all_filters(values)

    return filtered_values


def run():
    service = initialize_api_client()
    values = get_spreadsheet_data(service)
    if not values:
        print('No data found.')
    else:
        for row in values:
            print(row)


if __name__ == '__main__':
    run()
