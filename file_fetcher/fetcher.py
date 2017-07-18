"""This script fetches all urls in list.txt.

The idea is to reqrite this repsonse from kender, to use requests:
https://stackoverflow.com/a/863017
"""

from os.path import basename
from urllib.parse import urlsplit
import urllib
import requests

def url_to_name(url):
    """Returns a name from the url."""
    return basename(urlsplit(url)[2])

def download_file(url, filename_override=None):
    """Downloads a file from url. 

    :params: url ``str`` URL to fetch
    :params: filename_override ``str`` Manually set filename
    """
    filename = url_to_name(url)
    #request = urllib.Request(url) 
    response = requests.get(url)
    
    if response.info().has_key('Content-Disposition'):
        # If the response has Content-Disposition, take the filename from it
        filename = response.info()['Content-Disposition'].split('filename=')[1]
        if filename[0] == '"' or filename[0] == "'":
            filename = filename[1:-1]
    elif response.url != url:
        # if redirected, take name from final URL
        filename = url_to_name(response.url)

    file_to_save = open(filename, 'wb')
    file_to_save.write(response.read())
    file_to_save.close()

download_file("http://ligman.me/1IW1oab")
