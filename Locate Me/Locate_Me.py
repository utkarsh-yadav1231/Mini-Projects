
import urllib.request
import json
import re

# Get Public IP


def getPublicIP():
    data = str(urllib.request.urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urllib.request.urlopen(url)
data = json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

# Print Extracted Details

print ("\n We are tracking your Location... ")
print ("\n Your City : " + city)
print (" Your Region : " + region)
print (" Your Country : " + country)
print (" Your Location : " + location)