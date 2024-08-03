import requests
from datetime import datetime as dt

USERNAME = ""
TOKEN = "wyh1wvd8ZFG.wxc3aug"
GRAPH_ID = "graph1"
GRAPH_NAME = "Cycling Graph"

## 1. Create user account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## 2. Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}
graph_headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

## 3. Get the graph
## https://pixe.la/v1/users/a-know/graphs/test-graph

## 4. Post value to the graph
format_date = dt.now().strftime("%Y%m%d")
# format_date = dt(2024, 8, 2).strftime("%Y%m%d")

post_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_graph_params = {
    "date": format_date,
    "quantity": "10"
}

# response = requests.post(url=post_graph_endpoint, json=post_graph_params, headers=graph_headers)
# print(response.text)

## Optional: Put/Update the quantity already registered as a "Pixel". If target "Pixel" not exist, create a new "Pixel" and set quantity.
put_graph_endpoint = f"{post_graph_endpoint}/{format_date}"
put_graph_params = {
    "quantity": "10",
}
# response = requests.put(url=put_graph_endpoint, json=put_graph_params, headers=graph_headers)
# print(response.text)

## Optional: Delete pixel
delete_graph_endpoint = f"{post_graph_endpoint}/{format_date}"
# response = requests.delete(url=delete_graph_endpoint, headers=graph_headers)
# print(response.text)
