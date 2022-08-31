import requests
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Key", "Value"]

github_username  = "khatrivinay1"

#api url to grab public user data
api_url = f"https://api.github.com/users/{github_username}"

#send get request
response = requests.get(api_url)

#get the data in json or equivalent dict format
data =  response.json()

for key, value in data.items():
    table.add_row([key, value])

print(table)