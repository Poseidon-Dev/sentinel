from apps import Path, File
from shutil import copy2

__all__ = ['Put',]

class Put:
    
    def __init__(self, file, path:Path):
        self.path = path.path()
        self.file = file

    @property
    def dst(self):
        return f'{self.path}/'

    def check(self, count=0):
        from os.path import exists

        if count == 0:
            name = self.file.save_name
        else:
            name = self.file.save_name + str(count)

        if exists(self.dst + name):
            count += 1
            self.check(count)
        return self.dst + name

    def put(self):
        try:
            copy2(self.file.path, self.dst + self.file.save_name)
        except Exception as e:
            print(e)

    def __str__(self):
        return self.dst