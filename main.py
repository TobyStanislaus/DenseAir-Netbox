import argparse
from netbox import fetch_data, iterate_devices
import urllib3
import sys
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


parser = argparse.ArgumentParser(description='Filter Netbox results')
parser.add_argument('--filter', type=str, nargs='+',
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


data = fetch_data(args.api+"?", headers)

print('received', len(data), file=sys.stderr)

# results = iterate_devices(data, args.filter)

# print('-------------------------------------------------', file=sys.stderr)

results = json.dumps(data)
print(results, file=sys.stdout)
sys.exit(0)
