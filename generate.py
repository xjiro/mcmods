import json
import os

os.chdir(os.path.dirname(__file__))

files = [f for f in os.listdir('.') if f.endswith('.jar')]

with open('contents.json', 'w+') as f:
    json.dump(files, f)
