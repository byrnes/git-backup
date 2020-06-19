import os
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')
data_dir = parser.get('main', 'data_dir')

os.chdir(data_dir)

for d in os.scandir(data_dir):
    if not os.DirEntry.is_dir(d):
        continue

    os.chdir(d)
    os.system('git pull')