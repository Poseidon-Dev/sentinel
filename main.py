import threading
from sentinel import Path, Sentinel
from sentinel.files import RawFile

import core.config

if __name__ == '__main__':
    class AchFile(RawFile):
        """

        Adds additional support for AchFiles from the ERP
        including the total, count, and some name parsing
        """

        PATHS = core.config.ACH_PATHS
        
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

        @staticmethod
        def threads():
            paths = [
                {
                    'src' : Path(core.config.ACH_SRC_PATH, comp['src']),
                    'dst' : Path(core.config.ACH_DST_PATH, comp['dst'], core.config.ACH_DST_SUFFIX)
                }
                    for comp in core.config.COMPANIES
                ]

            sentinels = [Sentinel(path['src'], path['dst']) for path in paths]
            return [threading.Thread(target=s.run) for s in sentinels]

    class GarnFile(RawFile):
        """
        Adds additional support for AchFiles from the ERP
        including the total, count, and some name parsing
        """

        PATHS = core.config.GARN_PATHS
        
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

        @staticmethod
        def threads():
            paths = [
                {
                    'src' : Path(core.config.GAR_SRC_PATH, comp['src']),
                    'dst' : Path(core.config.GAR_DST_PATH, comp['dst'], core.config.GAR_DST_SUFFIX)
                }
                    for comp in core.config.COMPANIES
                ]

            sentinels = [Sentinel(path['src'], path['dst']) for path in paths]
            return [threading.Thread(target=s.run) for s in sentinels]

    threads = AchFile.threads() + GarnFile.threads()

    print("=" * 16 + " SENTINEL RUNNING " + "=" * 16)
    for t in threads:
        t.start()
  