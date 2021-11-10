import os.path
from apps.path import Path

from core.config import ACH_PATHS, GARN_PATHS

__all__ = ['File', 'AchFile', 'GarnFile',]

    
class RawFile():
    """
    Accepts a file from OS module to create an 
    encompassing class for easy manipulations
    """

    PATHS = None

    def __init__(self, f):
        self.file = f
        self.name = self.file.name
        self.stats = self.file.stat()
        self.size = self.stats.st_size
        self.local_path = self.file.path      
        self.path = os.path.abspath(self.local_path)


    @property
    def mod_date(self):
        """
        returns the last time modified in a datetime object
        """
        from datetime import datetime
        return datetime.fromtimestamp(self.stats.st_mtime)


    @property
    def acc_date(self):
        """
        returns the last time accessed in a datetime object
        """
        from datetime import datetime
        return datetime.fromtimestamp(self.stats.st_atime)


    @property
    def tree(self):
        """
        returns the abs path as a list
        """
        return self.path.split('\\')


    @property
    def ext(self):
        """
        returns the extention of a file
        """
        return self.name.split('.')[-1]


    @property
    def file_name(self):
        """
        returns the file name, allows for periods 
        in the filename
        """
        name = self.name.split('.')
        name.pop()
        return '.'.join(name)


    @property
    def _lines(self):
        """
        A simple list return of the File
        """
        if self.ext.lower() in ('csv', 'txt'):
            with open(self.path, 'r') as f:
                _lines = f.readlines()
            return _lines
        else:
            return []


    @property
    def count(self):
        return 0


    @property
    def total(self):
        return 0

    @property
    def save_name(self):
        """
        Returns the save name
        """
        return self.file_name
    

    @property
    def save_date(self):
        """
        Returns the save date
        """
        return self.mod_date


    def rawfile_type(self, f):
        return any(t in self.tree for t in self.PATHS)


    def __gt__(self, instance):
        """
        lexiographical comparison based on filename
        """
        return self.file_name.lower() > instance.file_name.lower()


    def __eq__(self, instance):
        """
        lexiographical comparison based on filename
        """
        return self.file_name.lower() == instance.file_name.lower()


    def __str__(self):
        return (
            f'file type: {self.__class__.__name__}\n'
            f'file: {self.file_name}\n'
            f'size: {self.size}\n'
        )    

class AchFile(RawFile):
    """

    Adds additional support for AchFiles from the ERP
    including the total, count, and some name parsing
    """

    PATHS = ACH_PATHS
    
    def __init__(self, f):
        super(AchFile, self).__init__(f)


    @property
    def count(self):
        """
        Searches from the rear of the file
        and looks for a line that starts with x
        Takes the line that is 2 lines above and 
        takes an integer value of the last 5
        """
        lines = self._lines
        if lines:
            count_line = ''
            last = len(lines) - 1
            while not count_line:
                for letter in lines[last][-2]:
                    if letter != 'X':
                        last -= 1
                    else:
                        count_line = lines[last-2]
            count_line = count_line.replace(' ','')[-5:]
            return int(count_line)
        else:
            return 0


    @property
    def save_name(self):
        """
        Extracts the save name given by the ERP system
        """
        return self.file.name.split('.')[0] 
    

    @property
    def save_date(self):
        """
        Extracts the save date given by the ERP system
        """
        return self.file.name.split('.')[1] 


    @property
    def total(self):
        """
        Returns the total amount in the file
        Looks from the back side of the file for a line that ends with X
        Once the line is found, it removes space and the x value from the line
        then takes the last 10 characters and converts to a decimal
        """
        lines = self._lines
        if lines:
            total_line = ''
            last = len(lines) - 1
            while not total_line:
                for letter in lines[last][-2]:
                    if letter != 'X':
                        last -= 1
                    else:
                        total_line = lines[last]
            total_line = total_line.replace('X', '').replace(' ','')[-10:]
            return int(total_line)/100
        else:
            0
            

    def __str__(self):
        str = super(AchFile, self).__str__()
        return (
            f'{str}'
            f'check count: {self.count}\n'   
            f'total: {self.total}\n'   
            f'ERP Name: {self.save_name}\n'   
            f'ERP Date: {self.save_date}\n'   
        )
    

class GarnFile(RawFile):
    """
    Adds additional support for AchFiles from the ERP
    including the total, count, and some name parsing
    """

    PATHS = GARN_PATHS
    
    def __init__(self, f):
        super(GarnFile, self).__init__(f)
        

    @property
    def count(self):
        """
        Searches from the rear of the file
        and looks for a line that starts with x
        Takes the line that is 2 lines above and 
        takes an integer value of the last 5
        """
        lines = self._lines
        if lines:
            count_line = ''
            last = len(lines) - 1
            while not count_line:
                for letter in lines[last][-2]:
                    if letter != 'X':
                        last -= 1
                    else:
                        count_line = lines[last-2]
            count_line = count_line.replace(' ','')[-5:]
            return int(count_line)
        else:
            return 0


    @property
    def save_name(self):
        """
        Extracts the save name given by the ERP system
        """
        prefix = 'APEFT PPD '
        file = self.file.name.split('.')[2] 
        file = f"20{file[-2:]}{file[:2]}{file[2:4]}"
        return prefix + file


    @property
    def total(self):
        """
        Returns the total amount in the file
        Looks from the back side of the file for a line that ends with X
        Once the line is found, it removes space and the x value from the line
        then takes the last 10 characters and converts to a decimal
        """
        lines = self._lines
        if lines:
            total_line = ''
            last = len(lines) - 1
            while not total_line:
                for letter in lines[last][-2]:
                    if letter != 'X':
                        last -= 1
                    else:
                        total_line = lines[last]
            total_line = total_line.replace('X', '').replace(' ','')[-10:]
            return int(total_line)/100
        else:
            0


    def __str__(self):
        str = super(GarnFile, self).__str__()
        return (
            f'{str}'
            f'ERP Name: {self.save_name}\n'   
            f'check count: {self.count}\n'   
            f'total: {self.total}\n'  
        )

class File:
    """
    Factory class for creating subclasses if criteria is met
    """
    def __new__(cls, f):
        for subcls in RawFile.__subclasses__():
            if subcls(f).rawfile_type(f):
                return subcls(f)

        return RawFile(f)

