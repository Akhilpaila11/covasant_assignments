import datetime
from pkg.file import File

fs = File(".")
print(fs.getMaxSizeFile(2))
print(fs.getLatestFiles(datetime.date(2025, 4, 1)))  


