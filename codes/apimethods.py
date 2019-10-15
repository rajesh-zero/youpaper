"""python file for api codes"""
import json
import requests

'''"""def search_api(parameter, value):
    """function for searchapi
    use syntax variablename_parseddata = search_api('s', search)"""
    headers = {}
    headers[parameter] = value
    headers['apikey'] = '16ee2b99'
    req = requests.get('http://www.omdbapi.com/?', params=headers)
    parsed_data = json.loads(req.text)
    return parsed_data"""'''

def search_api(header):
    """function for searchapi
    use syntax variablename_parseddata = search_api('s', search)"""
    headers = header
    headers['apikey'] = '16ee2b99'
    req = requests.get('http://www.omdbapi.com/?', params=headers)
    parsed_data = json.loads(req.text)
    return parsed_data
