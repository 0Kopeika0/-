import requests
import json

url = 'https://jsonkeeper.com/b/S62B'    
words = requests.get(url, verify=False)
WORDS = json.loads(words.text)