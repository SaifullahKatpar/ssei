
# script: api_manager.py
# class: APIManager, methods:  get_content_from_url(URL): response/text
# this script uses requests package for making HTTP requests to USGS services



# imports for APIManager
import requests


# this class defines methods for creating urls from key words,
# mapping owl classes to USGS APIs, etc. 
class APIManager:

    #parameters for the urls
    parameters = {}

    # base_urls
    base_urls = {}

    # takes a url and returns response in text
    def get_content_from_url(self,url):
        result = requests.get(url)
        return result.text
    




