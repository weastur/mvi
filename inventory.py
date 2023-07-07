#!/usr/bin/env python3

import os
import json
from hcloud import Client

HCLOUD_TOKEN = os.environ["HCLOUD_TOKEN"]


client = Client(token=HCLOUD_TOKEN)
servers = client.servers.get_all()
inventory = {
    "all": {
        "hosts": [],
    },
    "_meta": {
        "hostvars": {},
    },
}

for server in servers:
    inventory["all"]["hosts"].append(server.name)
    for lkey in server.labels.keys():
        if lkey.startswith("group_"):
            inventory.setdefault(lkey[6:], {}).setdefault("hosts", []).append(
                server.name
            )
    inventory["_meta"]["hostvars"][server.name] = {
        "ansible_host": server.public_net.ipv4.ip,
        "ansible_user": "ansible",
    }

print(json.dumps(inventory, indent=2))
