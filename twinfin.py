import sys
import requests

with open('key.txt','r') as f: key = f.read()
try:
    spot = sys.argv[1]
except:
    raise Exception("Spot ID not supplied!")

url = 'http://magicseaweed.com/api/{}/forecast/?spot_id={}'.format(key, spot)
response = requests.get(url).json()
if 'error_response' in response:
    raise Exception("Error {}: {}".format(response['error_response']['code'],
                                          response['error_response']['error_msg']))
height = response[0]['swell']['components']['primary']['height']
period = response[0]['swell']['components']['primary']['period']

output = 'Swell {} at {}'.format(height,period)
print(output)
