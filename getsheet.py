import pandas
import re

def convert_google_sheet_url(url):
    """Returns a converted url to match csv format for use with pandas module."""
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)
    return new_url

def get_sheet_from_url(url):
    """Returns a pandas sheet from a given url."""
    new_url = convert_google_sheet_url(url)
    return pandas.read_csv(new_url)



