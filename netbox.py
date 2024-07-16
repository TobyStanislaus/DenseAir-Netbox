import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url="https://netbox-dev.da.int/api/dcim/devices/10"
token="fe19f62cf80f7fba99230cffcf54307acaf8a90b"
#desiredKeys=['site','location','rack','position','tenant','device_type','description','airflow','serial','asset_tag','config_template']
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
        result=findDictData(dataDict[key]['url'],headers)
        return result
    
    if isinstance(dataDict[key],str) and dataDict[key][:8]=='https://' and dataDict[key]!=url:
        
        result=findDictData(dataDict[key],headers)
        return result
    
    else:
        return dataDict[key]

def findDictData(url,headers):
    dataDict=fetchData(url,headers)
    
    resultDict={}

    for key in dataDict:
        if isinstance(dataDict[key],list) and len(dataDict[key])>=1:
            dataDict[key]=dataDict[key][0]
        data=findCorrectData(dataDict,url,headers,key)
        resultDict[key]=data

    return resultDict

def run(query):
    resultDict=findDictData(url,headers)
    return resultDict[query]

#query=input("Input your query: ")
#print(run(query))