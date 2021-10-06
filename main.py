import threading
from concurrent.futures.thread import ThreadPoolExecutor
from apps import sentinel
from apps.sentinel import Sentinel

from core.config import ACH_SRC_PATH, COMPANIES

if __name__ == '__main__':
    sentinels = [Sentinel(ACH_SRC_PATH, comp['src']) for comp in COMPANIES]

    threads = []
    for s in sentinels:
        t = threading.Thread(target=s)
        threads.append(t)

    for t in threads:
        t.start()
    # threads = []
    # for s in sentinels:
    #     t = threading.Thread(s.run())
    #     threads.append(t)
        
    
    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()
    # with ThreadPoolExecutor(4) as exe:
    #     ordinal = 1
    #     for s in sentinels:
    #         exe.submit(s.run(), ordinal)


    # for company in COMPANIES:
    #     threads = [threading.Thread(target=Sentinel(ACH_SRC_PATH, company['src']).run())]

    # for t in threads:
    #     t.start()
        

    # threads = [threading.Thread(target=s.run()) for s in sentinels]
    # for thread in threads:
    #     thread.start()


    # for c in COMPANIES:
    #     s = Sentinel(ACH_SRC_PATH, c['src'])
    #     s.run()