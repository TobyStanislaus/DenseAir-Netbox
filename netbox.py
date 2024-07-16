import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url="https://netbox-dev.da.int/api/dcim/devices/9/"
token="ba3ac42a21fc1a55aeede388c446a0929f16fe99"
desiredKeys=['site','location','rack','position','tenant','device_type','description','airflow','serial','asset_tag','config_template']
headers = {
    'Content-Type':'application/json',
    'Authorization':'Token '+token
    }

def fetchData(url,headers):
    payload={}
    response=requests.request('GET',url,headers=headers,data=payload, verify=False)
    return response.json()

def findCorrectData(dataDict,url,headers,key):  
    #print(key)
    #print(dataDict[key])
   
    if (isinstance(dataDict[key],dict) and 'url' in dataDict[key]):
        result=findRawDictData(dataDict[key]['url'],headers)
        return result
    
    if isinstance(dataDict[key],str) and dataDict[key][:8]=='https://' and dataDict[key]!=url:
        result=findRawDictData(dataDict[key],headers)
        return result
    
    else:
        return dataDict[key]

def findRawDictData(url,headers):
    dataDict=fetchData(url,headers)
    
    resultDict={}

    for key in dataDict:

        data=findCorrectData(dataDict,url,headers,key)
        resultDict[key]=data

    return resultDict

resultDict=findRawDictData(url,headers)
print(resultDict)

