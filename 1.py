import argparse
import asyncio
import importlib.resources
import json
import logging
import os
import pathlib
import pprint
import sys
import time
import warnings

import httpx

from da_common.config import Config
import druid_interactions


async def api_query(client: httpx.AsyncClient, obj, info="count", params=None):
    if info:
        request = client.get(f"/{info}/{obj}", params=params)
    else:
        request = client.get(f"/{obj}", params=params)
    try:
        rv = await request
        return rv
    except Exception as e:
        warnings.warn(f"{e=}")


def main(args):
    print(f"Druid Interactions API demo version {druid_interactions.__version__}", file=sys.stderr)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    auth = httpx.BasicAuth(username=args.username, password=args.password)
    client = httpx.AsyncClient(auth=auth, base_url=args.api, verify=False)

    for obj in (
        # "alarm",
        # "alarm_definition",
        # "amf",
        # "bts",
        # "bts_lte_neighbor",
        # "ca_certificate",
        # "cbc_remote_mme",
        # "cn_hnb",
        # "cn_hnb_gw",
        # "crypto_profile",
        # "cmpv2_client",
        # "diameter_endpoint",
        # "eir",
        # "enbgw",
        # "enbgw_session",
        # "enodeb",
        # "enodeb_trx",
        # "enodeb_trx_lte_neighbor",
        # "enodeb_trx_lte_neighbor_in_use",
        # "features",
        # "gateway_msc_stat",
        # "gnb",
        # "group",
        # "gsm_config",
        # "gtp_proxy",
        # "gtp_proxy_destination",
        # "hnb",
        # "hnb_trx",
        # "hnb_trx_lte_neighbor",
        # "hnb_trx_lte_neighbor_in_use",
        # "ip_data_record",
        # "ip_route",
        "ipsec_child_config",
        "ipsec_child_config_proposal",
        # "ipsec_connection",
        "ipsec_certificate",
        "ipsec_ike_config_proposal",
        # "ipsec_ike_sa",
        # "ipsec_shared_secret",
        "ipsec_peer_config",
        "ipsec_private_key",
        "ipsec_secure_association",
        "ipsec_proposal",
        # "ip_sm_gw",
        # "ipv4_pool",
        # "lgw_tunnel",
        # "lmf",
        # "local_access_gateway",
        # "mgw_ctrl_flow_stats",
        # "mobile_equipment_identity",
        # "mme_activity",
        # "mme_stat",
        # "net_device",
        # "network_slice",
        # "nms",
        "pgw_pdn_connection",
        # "plmn",
        # "radio_zone",
        # "raemis",
        "s1_client",
        # "s1_server",
        # "s1_server_enb",
        # "s1_server_enb_grp",
        # "s1_server_enodeb_trx",
        # "s1_lgw",
        # "sbi_server",
        # "sgs_server",
        # "sgw",
        # "sgw_session",
        # "signalling_gateway",
        # "smf",
        # "smsf",
        # "subscription_profile",
        # "trx",
        # "udm",
    ):
        for info in ("", "schema", "count"):
            rv = loop.run_until_complete(api_query(
                client, obj, info=info,
            ))
            time.sleep(0.5)  # <Response [429 Too Many Requests]>
            try:
                data = rv.json()
                print("\n\n", rv.url, sep="")
                print("=" * len(str(rv.url)), "\n", sep="")
            except (AttributeError, json.JSONDecodeError):
                data = rv

            if info == "count":
                print(rv and rv.url, data, file=sys.stderr)

            pprint.pprint(data)

            sys.stdout.flush()
    loop.run_until_complete(client.aclose())
    return 0


def parser(default_config=""):
    default_api = "https://192.168.80.35:443/api"
    rv = argparse.ArgumentParser(usage=__doc__)
    rv.add_argument(
        "--api", default=default_api,
        help=f"URL path to API root [{default_api}]."
    )
    rv.add_argument("--username", default="dhaynes", help="API user")
    rv.add_argument("--password", default=os.getenv("API_PASSWORD", ""), help="API password")
    return rv


def run():
    config = importlib.resources.files("druid_interactions.cfg").joinpath("starter.toml")
    p = parser(default_config=config)
    args = p.parse_args()
    rv = main(args)
    sys.exit(rv)


if __name__ == "__main__":
    run()
