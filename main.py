
import requests
from datetime import datetime

USERNAME = "varsha3"
TOKEN="Varsha2023"
GRAPH_ID = "graph1"
# pixela endpoint
pixelaEndpoint = "https://pixe.la/v1/users"
parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url = pixelaEndpoint,json= parameters)
print(response.text)
# graph endpoint

graphEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"
graph_params={
    "id":"graph1",
    "name":"weight chart",
    "unit":"Kg",
    "type":"float",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# res = requests.post(url=graphEndpoint,json=graph_params,headers=headers)
# print(res.text)
today = datetime.now()

pixelEndpoint= f"{pixelaEndpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params ={
    "date":today.strftime("%Y%m%d"),
    "quantity":"56.5"
    # "quantity":
}
pixel_header = {
    "X-USER-TOKEN": TOKEN
}
resp = requests.post(url=pixelEndpoint,json=pixel_params,headers=pixel_header)
print(resp.text)

# PUT request
putEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{GRAPH_ID}/{20230417}"
putHeader = {
    "X-USER-TOKEN": TOKEN
}
putBody = {
    "quantity":"56.9"
}
respon = requests.put(url=putEndpoint,json= putBody,headers=putHeader)
print(respon.text)
