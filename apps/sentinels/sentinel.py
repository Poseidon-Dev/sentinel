import os, shutil
import time

from core.config import ACH_DST_PATH, ACH_DST_SUFFIX, ACH_SRC_PATH, COMPANIES, DELAY_INTERVAL
from core.utils import Timer, send_email
# from apps.sentinel import File

class File:
    def __init__(self, file, directory):
        self.file = file
        self.directory = directory
        
    @property
    def full_name(self):
        return self.file.name

    @property
    def stored_name(self):
        return self.file.name.split('.')[0] 

    @property
    def size(self):
        return self.file.stat().st_size

    @property
    def date(self):
        from datetime import datetime
        return datetime.fromtimestamp(self.file.stat().st_mtime)

    @property
    def path(self):
        return self.file.path

    def __str__(self):
        return self.path

class Snapshot:

    def __init__(self, src_path_dir, src_subdir=''):
        self.src_path_dir = src_path_dir
        self.src_subdir = src_subdir

    @property
    def path(self):
        if not self.src_subdir:
            path = self.src_path_dir
        else:
            path = self.src_path_dir + '/' + self.src_subdir
        return path

    def snapshot(self):
        # print(self.path)
        dirs = os.scandir(self.path)
        snapshot = [
            File(file, self.path)
            for file in dirs
        ]
        # for file in snapshot[:5]:
        #     print(file)
        return snapshot

class Put:

    def __init__(self, dst_dir, file:File, dst_subdir='', dst_suffix=''):
        self.dst_dir = dst_dir
        self.file = file
        if dst_subdir:
            self.dst_subdir =  '/' + dst_subdir
        else:
            self.dst_subdir = dst_subdir
        if dst_suffix:
            self.dst_suf = '/' + dst_suffix
        else: 
            self.dst_suf = dst_suffix

    @property
    def dst(self):
        return f'{self.dst_dir}{self.dst_subdir}{self.dst_suf}'

    def put(self):
        try:
            shutil.copy2(self.file.path, self.dst + self.file.stored_name)
        except Exception as e:
            print(e)

    def __str__(self):
        return f'{self.dst}/{self.file.full_name}'


class AbstractSentinel:
    DELAY_INTERVAL = 20
   
    def snapshot(self):
        pass

    def compare(self):
        pass

    def run(self):
        pass

class Sentinel(AbstractSentinel):

    def __init__(self, src_path, dst_path, src_subdir='', dst_subdir=''):
        self.src_path = src_path
        self.src_subdir = src_subdir
        self.dst_path = dst_path
        self.dst_subdir = dst_subdir


    def snapshot(self):
        return Snapshot(self.src_path, self.src_subdir)

    def compare(self, pre, pro):
        compare = {}
        pre_set = set(file.full_name for file in pre)
        pro_set = set(file.full_name for file in pro)

        created = list(pro_set-pre_set)
        deleted = list(pre_set-pro_set)

        compare['created'] = [f for f in pro if f.full_name in created]
        compare['deleted'] = [f for f in pre if f.full_name in deleted]

        return compare
        
    def fetch_compare(self):
        pre = [file for file in self.snapshot().snapshot()]
        time.sleep(self.DELAY_INTERVAL)
        post = [file for file in self.snapshot().snapshot()]
        return self.compare(pre, post)


    def run(self):
        changes = self.fetch_compare()
        for status, files in changes.items():
            if files:
                if status == 'created':
                    for file in files:
                        print(f'{self.dst.subdir}: {file.stored_name}')
                        message = f'{file.stored_name} for company {self.dst_subdir} was found. File transfer complete'
                        send_email('Payroll File Transfer', message)
                        put = Put(self.dst_path, file, self.dst_subdir, ACH_DST_SUFFIX).put()


    def thread(self):
        while True:
            self.run()            
