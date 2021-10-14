from apps import Path, File
from shutil import copy2
import os.path

__all__ = ['Put',]

class Put:
    
    APPENDS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self, file, path:Path):
        self.path = path.path()
        self.file = file
        self.dst = self.check(f'{self.path}/{self.file.save_name}')

    def check(self, path, count=0):
        while os.path.exists(path):
            if path[-1] in self.APPENDS:
                path = path[:len(path)-1] + self.APPENDS[count]
            else:
                path = path + self.APPENDS[count]
            count +=1
        return path


    def put(self):
        try:
            copy2(self.file.path, self.dst)
        except Exception as e:
            return e

    def __str__(self):
        return self.dst