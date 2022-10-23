import requests
from datetime import datetime

# load_dotenv will be used to load the .env file to the environment variables.
from dotenv import load_dotenv
# os will be used to refer to those variables in the code
import os

# Credentials
load_dotenv(".env")  # This will load the .env file

# https://pixe.la/
# https://docs.pixe.la/
# https://requests.readthedocs.io/en/latest/api/

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

##  1 Creates an user acount on pixela. After creating the user we can comment below two lines of code
# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)  # Let's visit https://pixe.la/@{USERNAME} , it is your profile page!"

# 2 Create a graph definition
REQUEST_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# graph_config = {
#     "id": "graph1",
#     "name": "Reading",
#     "unit": "Pages",
#     "type": "int",
#     "color": "ajisai",
# }

pixela_graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=REQUEST_HEADERS)
# print(response.text)

# 3 To see the created graph go to: https://pixe.la/v1/users/abeldrigo/graphs/graph1.html

# 4 Post value to the graph
graph_id = "graph1"
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}"
today = (datetime.today()).strftime("%Y%m%d")
print(today)
pixel_data = {
    "date": today,
    "quantity": "30",
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=REQUEST_HEADERS)
print(response.text)

# Update pixel
pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}/{today}"
pixel_update_data = {
    "quantity": "50",
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=REQUEST_HEADERS)
print(response.text)

response = requests.delete(url=pixel_update_endpoint, json=pixel_update_data, headers=REQUEST_HEADERS)
print(response.text)

