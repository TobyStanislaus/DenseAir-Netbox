import argparse
from netbox import *
import urllib3
import sys
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



parser = argparse.ArgumentParser(description='Filter Netbox results')
parser.add_argument('--filter', type=str,
                    help='Filter the fetched data from the netbox APIs')

parser.add_argument('--token', type=str,
                    help='Input your API token for the relevant API')


parser.add_argument('--api', type=str,
                    help='Input the api URL that you wish to search from')

args = parser.parse_args()

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + args.token
    }


url = build_url(args.api, args.filter)

print('Contacting Netbox at', url, file=sys.stdout)

try:
    data = fetch_data(url, headers)
except Exception:
    print('Invalid URL', file=sys.stderr)
    sys.exit(1)

if len(data) == 1:
    print('Invalid filters', file=sys.stderr)
    sys.exit(1)

print('Received:', len(data), 'objects', file=sys.stdout)

output = open("results.txt", "w")
response = data['results']
results = json.dumps(response, indent=4)
print(results, file=output)

output.close()

sys.exit(0)
# search all references to build a huge file
#main.py --api https://demo.netbox.dev/api/dcim/devices --token c98be45069605e1713858a451012c6905c4a13be --filter juniper