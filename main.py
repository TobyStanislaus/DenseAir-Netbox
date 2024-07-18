import argparse
from netbox import run
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://netbox-dev.da.int/api/dcim/devices/10/"
token = "5ce339f64325ecfda8250344636943e24297cf62"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+token
    }


parser = argparse.ArgumentParser(description='Filter Netbox results')
parser.add_argument('--filter', type=str, nargs='+',
                    help='Filter the fetched data from the netbox APIs')

args = parser.parse_args()
print(run(args.filter, url, headers))
