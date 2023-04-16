
import requests

pixelaEndpoint = "https://pixe.la/v1/users"
parameters = {
    "token":"Varsha2023",
    "username":"varsha3",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url = pixelaEndpoint,json= parameters)
print(response.text)
