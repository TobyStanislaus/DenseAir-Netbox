import argparse
from netbox import collect_all_data
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


parser = argparse.ArgumentParser(description='Filter Netbox results')
parser.add_argument('--filter', type=str, nargs='+',
                    default='',
                    help='Filter the fetched data from the netbox APIs')

parser.add_argument('--token', type=str,
                    help='Input your API token')


parser.add_argument('--api', type=str,
                    default="https://netbox-dev.da.int/api/dcim/devices/10/",
                    help='Input the api you wish to search from')

args = parser.parse_args()

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+args.token
    }

print("Accessing Netbox...", file=sys.stderr)
print(collect_all_data(args.filter, args.api, headers))
sys.exit(0)

