import requests
from termcolor import colored


ip = input(str("Enter the ip you would like to look up: "))

## single ip request
# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
#
# print(response['lat'])
# print(response['lon'])

# batch ip request

response = requests.post("http://ip-api.com/batch", json=[
  {"query": ip},
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")

print(colored('task completed', 'red'))
