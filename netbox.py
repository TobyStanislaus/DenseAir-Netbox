import requests
import json


def fetchData(url, headers):
    payload = {}
    response = requests.request('GET', url,
                                headers=headers, data=payload, verify=False)
    return response.json()


def findCorrectData(dataDict, url, headers, key):
    if (isinstance(dataDict[key], dict) and 'url' in dataDict[key]):
        result = findDictData(dataDict[key]['url'], headers)
        return result

    validURL = (isinstance(dataDict[key], str) and dataDict[key][:8] == 'http')
    if validURL and dataDict[key] != url:
        result = findDictData(dataDict[key], headers)
        return result

    else:
        return dataDict[key]


def findDictData(url, headers):
    dataDict = fetchData(url, headers)
    resultDict = {}
    for key in dataDict:
        if isinstance(dataDict[key], list) and len(dataDict[key]) >= 1:
            dataDict[key] = dataDict[key][0]
        data = findCorrectData(dataDict, url, headers, key)
        resultDict[key] = data

    return resultDict


def run(args, url, headers):
    resultDict = findDictData(url, headers)
    desiredDict = {}
    for arg in args:
        desiredDict[arg] = resultDict[arg]

    resultJSON = json.dumps(desiredDict)
    return resultJSON


'''
def demoFetch(url,headers):
    res=fetchData(url,headers)
    print('{')
    for term in ['id','location','url']:
        print(term,':',res[term])
    print('}')
'''


