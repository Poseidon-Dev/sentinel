import os, shutil
import asyncio
import time

from core.config import ACH_DST_PATH, ACH_DST_SUFFIX, ACH_SRC_PATH, COMPANIES, DELAY_INTERVAL
from apps.sentinel import File
from apps.sentinel.utils import loop

class Sentinel:

    def __init__(self):
        self.directory = ACH_SRC_PATH
        self.destination = ACH_DST_PATH
        self.companies = COMPANIES
        self.delay_interval = DELAY_INTERVAL

    def delay(self):
        return time.sleep(self.delay_interval)

    def snapshot(self, company):
        dirs = os.scandir(ACH_SRC_PATH + company)
        snapshot = [        
            File(file, ACH_SRC_PATH + company)
            for file in dirs]
        return snapshot


    def check(self):
        for company in COMPANIES:
            print('checking company :', company[0])
            _h = self.snapshot(company[0])
            self.delay()
            _n = self.snapshot(company[0])

            history = set([file.stored_name for file in _h])
            new = set([file.stored_name for file in _n])

            created = list(new - history)
            deleted = list(history - new)

            if created:
                return ('created', [(f.path, f.stored_name) for f in _n if f.stored_name in created], company)
            
            if deleted:
                return ('deleted', [(f.path, f.stored_name) for f in _h if f.stored_name in deleted], company)


    def run(self):
        print('=========== RUNNING PAYROLL SENTINEL ===========')
        while True:
            try:
                check = self.check()
                if check:
                    status, files, company = check
                    if status == 'created':
                        for file in files:
                            print(ACH_DST_PATH + company[1] + ACH_DST_SUFFIX)
                            shutil.copy2(file[0], ACH_DST_PATH + company[1] + ACH_DST_SUFFIX + file[1] )
                    print(status, files)
            except KeyboardInterrupt:
                print('Closing Payroll Watchdog')
                exit()
            except TypeError:
                pass


        

    
