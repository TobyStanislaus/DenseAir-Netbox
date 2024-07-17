import requests
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetchData(url,headers):
    payload={}
    response=requests.request('GET',url,headers=headers,data=payload, verify=False)
    return response.json()

def findCorrectData(dataDict,url,headers,key):  
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

def generateResultDict():
    url="https://netbox-dev.da.int/api/dcim/devices/10"
    token=""
    #desiredKeys=['site','location','rack','position','tenant','device_type','description','airflow','serial','asset_tag','config_template']
    headers = {
        'Content-Type':'application/json',
        'Authorization':'Token '+token
        }
    
    resultDict=findDictData(url,headers)
    return resultDict

def run(args):
    resultDict=generateResultDict()
    for arg in args: 
        if isinstance(resultDict[arg],dict):
            print(arg)
            for key in resultDict[arg]:
                print(str(key)+ ' - ' +str(resultDict[arg][key]))
        else:
            print(arg)
            print(str(resultDict[arg]))
        print('-----------------------------------------')


parser = argparse.ArgumentParser(description='Filter Netbox results')
parser.add_argument('--filter', type=str,nargs='+', help='Filter the fetched data from the netbox APIs')

args = parser.parse_args()

run(args.filter)