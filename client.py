import requests

host = "http://127.0.0.1:5491"
registered = host + "/api/registered"
ask = host + "/api/ask"

params = {
    "name": "MiaoPaSi",
    "host": "127.0.0.1",
    "port": "12345",
}
r = requests.post(registered, data=params)
print(r.text)

r = requests.post(ask, data={"name": params.get("name")})
print(r.text)
