import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url="https://netbox-dev.da.int/api/dcim/devices/9/"
token="2b9ab16a20cc1d8cd5cc73039d3c818711a0fb35"
desiredKeys=['site','location','rack','position','tenant','device_type','description','airflow','serial','asset_tag','config_template']
headers = {
    'Content-Type':'application/json',
    'Authorization':'Token '+token
    }

def fetchData(url,headers):
    payload={}
    response=requests.request('GET',url,headers=headers,data=payload, verify=False)
    return response.json()



def findCorrectData(dataDict,headers):

    return dataDict[key]

dataDict=fetchData(url,headers)

resultDict={}
for key in desiredKeys:

    data=findCorrectData(dataDict,headers)
    resultDict[key]=data
    print(data)


