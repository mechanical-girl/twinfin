import sys
import requests

with open('key.txt','r') as f: key = f.read()
try:
    spot = sys.argv[1]
except:
    raise Exception("Spot ID not supplied!")

url = 'http://magicseaweed.com/api/{}/forecast/?spot_id={}'.format(key, spot)
response = requests.get(url).json()
output = '{} at {}'.format(response[0]['swell']['components']['primary']['height'],response[0]['swell']['components']['primary']['period'])
print(output)
