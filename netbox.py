import requests
import json
import sys


def fetch_data(url, headers):
    '''
    Fetches data from netbox apis
    '''
    payload = {}

    response = requests.request('GET', url,
                                headers=headers,
                                data=payload,
                                verify=False)

    return response.json()


def iterate_devices(data, filter):
    '''
    This will run through the devices in the data[results].
    Then, it uses check_device to choose if it should be appended to results
    (its in the filter).
    '''

    results = []
    for device in data['results']:

        result = check_device(filter, device, results)
        if result:
            results.append(result)
    return results


def check_device(filter, device, results):
    '''
    Checks if it contains the filter string in any of
    the values in the device dictionary.
    '''
    for key in device:
        if str(device[key])[:len(filter)] != filter:
            pass
        elif device not in results:
            return device


def show_result(result):
    print(' ')
    print(' ')
    print(' ')
    for key in result:
        print(key, ':', result[key])


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
        newDict = fetch_data(dataDict[key], headers)
        result = find_dict_data(newDict, dataDict[key]['url'], headers)
        return result

    validURL = (isinstance(dataDict[key], str) and dataDict[key][:4] == 'http')
    if validURL and dataDict[key] != url:
        newDict = fetch_data(dataDict[key], headers)
        result = find_dict_data(newDict, dataDict[key]['url'], headers)
        return result

    else:
        return dataDict[key]


def find_dict_data(dataDict, url, headers):
    '''
    Collects and iterates through a dictionary
    fetched by the fetch_data function
    '''

    resultDict = {}
    for key in dataDict:
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
