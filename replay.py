import json
import random

print("[*] Generating replay trace...")
replay = {
    "session": hex(random.randint(100000, 999999)),
    "target": "198.51.100.23",
    "packets": [random.randint(1000, 5000) for _ in range(10)]
}
print(json.dumps(replay, indent=2))
