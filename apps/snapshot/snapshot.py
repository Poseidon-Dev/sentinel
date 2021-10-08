from apps import File

class Path:
    """
    Simple string concantenation to create
    a path name
    """
    def __init__(self, path_dir, *subdirs):
        self.dir = path_dir
        self.subdirs = subdirs

    def path(self):
        path = self.dir
        for sub in self.subdirs:
            path += '/' + sub
        return path

    def __str__(self):
        return self.path()


class Snapshot:
    """
    A current list of files within a specified directory
    """

    def __init__(self, path:Path):
        self.files = self.snap(path)

    def list_snap(self):
        """ 
        Prints a list of File objects from a snapshot
        """
        for f in self.files:
            print(f)

    def snap(self, path:Path):
        from os import scandir
        return [File(f) for f in scandir(path.path())]



