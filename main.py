import threading
from apps import Path, Sentinel

from core.config import ACH_DST_PATH, ACH_SRC_PATH, COMPANIES, ACH_DST_SUFFIX

if __name__ == '__main__':

    paths = [
        {
            'src' : Path(ACH_SRC_PATH, comp['src']),
            'dst' : Path(ACH_DST_PATH, comp['dst'], ACH_DST_SUFFIX)
        }
         for comp in COMPANIES
        ]
    
    drop = Path('C:\Apps\TESTDUMP')
    sentinels = [Sentinel(path['src'], path['dst']) for path in paths]
    threads = [threading.Thread(target=s.run) for s in sentinels]

    print("=" * 16 + " SENTINEL RUNNING " + "=" * 16)
    for t in threads:
        t.start()
  