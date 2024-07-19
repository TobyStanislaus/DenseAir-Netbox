import requests


def build_url(api, filter_string):
    return api + '?manufacturer=' + filter_string.lower()


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
