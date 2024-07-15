import requests

url="https://netbox-dev.da.int/api/"
payload={}
headers = {
    'Content-Type':'application/json',
    'Authorization':'Token 2b9ab16a20cc1d8cd5cc73039d3c818711a0fb35'
}

response=requests.request('GET',url,headers=headers,data=payload)

print(response.json())