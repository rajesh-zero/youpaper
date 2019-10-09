"""python file for api codes"""
import json
import requests

def search_api(search):
    """function for searchapi"""
    headers = {}
    headers['s'] = search
    headers['apikey'] = '16ee2b99'
    req = requests.get('http://www.omdbapi.com/?', params=headers)
    parsed_data = json.loads(req.text)
    return parsed_data
