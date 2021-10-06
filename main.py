import threading
from apps.sentinel import Sentinel

from core.config import ACH_DST_PATH, ACH_SRC_PATH, COMPANIES

if __name__ == '__main__':
    sentinels = [Sentinel(ACH_SRC_PATH, ACH_DST_PATH, src_subdir=comp['src'], dst_subdir=comp['dst']) for comp in COMPANIES]

    threads = []
    for s in sentinels:
        t = threading.Thread(target=s.thread)
        threads.append(t)

    print("=" * 16 + " SENTINEL RUNNING " + "=" * 16)
    for t in threads:
        t.start()
   