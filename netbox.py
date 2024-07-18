import requests
import json
import sys


def fetch_data(url, headers):
    '''
    Fetches data from netbox apis
    '''
    payload = {}
    try:
        response = requests.request('GET', url,
                                    headers=headers,
                                    data=payload,
                                    verify=False)
    except:
        sys.exit(2)

    return response.json()


def find_correct_data(dataDict, url, headers, key):
    '''
    Recieves a certain key in the dictionary,
    and we use this value to find dataDict[key], which could be:
    - A dictionary with an url embedded
    - A url itself
    - a value

    If there is a url within it, we must process it further and find
    all the data within that url
    '''
    if (isinstance(dataDict[key], dict) and 'url' in dataDict[key]):
        result = find_dict_data(dataDict[key]['url'], headers)
        return result

    validURL = (isinstance(dataDict[key], str) and dataDict[key][:4] == 'http')
    if validURL and dataDict[key] != url:
        result = find_dict_data(dataDict[key], headers)
        return result

    else:
        return dataDict[key]


def find_dict_data(url, headers):
    '''
    Collects and iterates through a dictionary
    fetched by the fetch_data function
    '''
    dataDict = fetch_data(url, headers)
    resultDict = {}
    for key in dataDict:
        if isinstance(dataDict[key], list) and len(dataDict[key]) >= 1:
            dataDict[key] = dataDict[key][0]
        data = find_correct_data(dataDict, url, headers, key)
        resultDict[key] = data

    return resultDict


def collect_all_data(filters, url, headers):
    '''
    The main function- it sets off the other functions
    to collect and refine the data from netbox apis.
    '''
    resultDict = find_dict_data(url, headers)
    desiredDict = {}

    for filter in filters:
        desiredDict[filter] = resultDict[filter]

    resultJSON = json.dumps(desiredDict)
    return resultJSON

def all_for_one(data,filter):
    for device in data['results']:
        if device['name'][:len(filter)] == filter:
            print(device)
            print('')
 
   