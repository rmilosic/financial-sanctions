import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import os

from .save import save_file_to_source_data

def download_eu_fsd():
    """
    Downloads EU FSD list
    
    Returns
    string: path to file
    """
    # save source file to local storage or s3 

    # # URL of the webpage to extract the link from
    # url = 'http://example.com'

    # # Send a GET request to the URL and get the webpage HTML
    # response = requests.get(url)
    # html = response.content

    # # Parse the HTML using BeautifulSoup
    # soup = BeautifulSoup(html, 'html.parser')

    # # Find the first link on the webpage
    # link = soup.find('a')['href']

    # # Print the link
    # print(link)


    # URL of the file to be downloaded
    url = 'https://webgate.ec.europa.eu/fsd/fsf/public/files/xmlFullSanctionsList/content?token=n004abow'

    return save_file_to_source_data(url, "eu_fsd.xml")