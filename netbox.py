import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url="https://netbox-dev.da.int/api/dcim/devices/9/"
token="2b9ab16a20cc1d8cd5cc73039d3c818711a0fb35"
desiredKeys=['region','site','location','rack','position','tenant','device_type','description','airflow','serial','asset_tag','config_template']

def fetchData(url,token):
    payload={}
    headers = {
        'Content-Type':'application/json',
        'Authorization':'Token '+token
        }
    response=requests.request('GET',url,headers=headers,data=payload, verify=False)
    
    response=fetchData(url,token)
    data=response.json()
    specifyData(desiredKeys,data,token)


def specifyData(desiredKeys,data,token):
    result=[]
    for key in data:
        if key in desiredKeys:
   
            if isinstance(data[key],dict):
                try:
                    print(fetchData(data[key]['url'],token).json())
                except:
                    pass
    return result



