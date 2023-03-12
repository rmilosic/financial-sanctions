import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import os


def save_file_to_source_data(url, filename):

    now = datetime.datetime.now()
    formatted_datetime = now.strftime('%Y-%m-%d')

    # # Path where the downloaded file will be saved
    save_path = f'data/source/{formatted_datetime}'

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # # Download the file from the URL and save it to the local filesystem
    final_path, _ = urllib.request.urlretrieve(url, os.path.join(save_path, filename))

    return final_path