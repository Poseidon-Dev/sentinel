import threading
from apps import Path, Sentinel

from core import defaults, config

def ach_threads():
    paths = [
        {
            'src' : Path(defaults.ACH_SRC_PATH, comp['src']),
            'dst' : Path(defaults.ACH_DST_PATH, comp['dst'], defaults.ACH_DST_SUFFIX)
        }
            for comp in config.COMPANIES
        ]

    sentinels = [Sentinel(path['src'], path['dst']) for path in paths]
    return [threading.Thread(target=s.run) for s in sentinels]

def garnishment_threads():
    paths = [
        {
            'src' : Path(defaults.GAR_SRC_PATH, comp['src']),
            'dst' : Path(defaults.GAR_DST_PATH, comp['dst'], defaults.GAR_DST_SUFFIX)
        }
            for comp in config.COMPANIES
        ]

    sentinels = [Sentinel(path['src'], path['dst']) for path in paths]
    return [threading.Thread(target=s.run) for s in sentinels]

threads = ach_threads() + garnishment_threads()
