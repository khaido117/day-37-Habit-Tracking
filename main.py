import requests 
from datetime import datetime

USERNAME = "khai"
TOKEN = "1a1a1a1a1a1a1a1a"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixela_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_pixel = {
    "date": "20231020",
    "quantity": "20"
}

# response = requests.post(url=pixela_endpoint, json=graph_pixel, headers= header )
# print(response.text)

date_endpoint = f"{pixela_endpoint}/20231021"

date_config = {
    "quantity": "12"
}

# response = requests.put(url=date_endpoint, json= date_config,headers=header)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/20231021"

response = requests.delete(url=date_endpoint,headers=header)
print(response.text)