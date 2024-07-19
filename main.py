import argparse
from netbox import fetch_data, build_url
import urllib3
import sys
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


parser = argparse.ArgumentParser(description='Filter Netbox results')
parser.add_argument('--filter', type=str,
                    default='',
                    help='Filter the fetched data from the netbox APIs')

parser.add_argument('--token', type=str,
                    help='Input your API token')


parser.add_argument('--api', type=str,
                    default="https://netbox-dev.da.int/api/dcim/devices/",
                    help='Input the api you wish to search from')

args = parser.parse_args()

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+args.token
    }


url = build_url(args.api, args.filter)

print('Contacting Netbox at', url, file=sys.stderr)


data = fetch_data(url, headers)

if len(data) == 1:
    print('Invalid filters', file=sys.stderr)
    sys.exit(1)

print('Received:', len(data), 'objects', file=sys.stderr)
results = json.dumps(data)
print(results, file=sys.stdout)

sys.exit(0)
