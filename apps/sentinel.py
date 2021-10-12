from apps import File, Path, Put, Snapshot
import time

from core.config import DELAY_INTERVAL
from core.utils import send_email

__all__ = ['Sentinel']

class Sentinel:

    INTERVAL = DELAY_INTERVAL

    def __init__(self, src_path:Path, dst_path:Path):
        self.src = src_path
        self.dst = dst_path

    def snap(self):
        """
        Returns a snapshot of the current src directory
        """
        return Snapshot(self.src)

    def changes(self, interval=INTERVAL):
        """
        Returns the changes in a given directory that happened 
        within the specified interval
        """
        snap1 = self.snap()
        time.sleep(interval)
        snap2 = self.snap()
        return snap1.compare(snap2)

    def transfer_files(self):
        """
        If changes are found, place them in the Put directory
        """
        changes = self.changes()
        for status, files in changes.items():
            if status == 'created':
                for f in files:
                    print(f)
                    # send_email('Payroll File Transfer', f.__str__())
                    put = Put(f, self.dst).put()
                    print(put)

    def run(self):
        while True:
            self.transfer_files()


    