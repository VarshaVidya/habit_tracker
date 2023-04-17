
import requests

USERNAME = "varsha3"
TOKEN="Varsha2023"
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
res = requests.post(url=graphEndpoint,json=graph_params,headers=headers)
print(res.text)
