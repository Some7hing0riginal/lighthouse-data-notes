import os
import requests
import pprint
import json
import html
import urllib

def loadJson():
    # Opening JSON file
    f = open('auth.json',)
    data = json.load(f)
    return data

base_url = "https://api.themoviedb.org/3/search/movie?api_key=18fc6bf4a1b093d18a5afbb816a8984b&query=The+Matrix"
def makeRequest(url):
    # don't forget package os
    app_id = os.environ["app_id"]
    app_key = os.environ["app_key"]
    url_append = f'?app_id={app_id}&app_key={app_key}' 


    # We send the request to the API
    # NOTE: if you don't have your APP_KEY, run this without the url_append
    res = requests.get(url)

    # We can check if the request was successful
    if res.status_code != 200 and res.status_code != 300:
        print(f"Unsuccessful request. Error code {res.status_code}")
        return res.status_code
    else:
        return res