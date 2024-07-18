import argparse
from netbox import fetch_data, iterate_devices, present_results
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
                    default="https://netbox-dev.da.int/api/dcim/devices/",
                    help='Input the api you wish to search from')

args = parser.parse_args()

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+args.token
    }

data = fetch_data(args.api, headers)
results = iterate_devices(data, args.filter[0])

present_results(results)

sys.exit(0)

