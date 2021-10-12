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