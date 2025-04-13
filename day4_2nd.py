import os
import datetime
class File:
    def __init__(self, path):
        self.path = path
    def getMaxSizeFile(self, n=1):
        files = [
            (f, os.path.getsize(os.path.join(self.path, f)))
            for f in os.listdir(self.path)
            if os.path.isfile(os.path.join(self.path, f))
        ]
        files.sort(key=lambda x: x[1], reverse=True)
        return [f[0] for f in files[:n]]
    def getLatestFiles(self, since_date):
        result = []
        for f in os.listdir(self.path):
            full_path = os.path.join(self.path, f)
            if os.path.isfile(full_path):
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(full_path)).date()
                if mtime > since_date:
                    result.append(f)
        return result


import datetime
from day4_2nd import File

fs = File(".")
print(fs.getMaxSizeFile(2))
print(fs.getLatestFiles(datetime.date(2025, 4, 1)))  


