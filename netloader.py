import json
import random
from etc import config

class Node:
    def __init__(self, ip, region):
        self.ip = ip
        self.region = region

    def __repr__(self):
        return f"{self.ip}@{self.region}"

with open("etc/nodes.list") as f:
    nodes = [Node(ip.strip(), random.choice(["us", "eu", "apac"])) for ip in f.readlines() if ip.strip()]

print("[*] Loaded", len(nodes), "nodes")
