import requests, json

FiveSimProtocolApiKey = ""
token = FiveSimProtocolApiKey

def buy(country, operator, product):
    global token
    abc = requests.get("https://5sim.net/v1/user/buy/activation/" + country + "/" + operator + "/" + product, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/json"
    })
    json_ = json.loads(abc.text)
    data = {
        "id": json_["id"],
        "phone": json_["phone"],
        "country": json_["country"],
        "operator": json_["operator"],
        "status": json_["status"]
    }
    return data

def get(id):
    global token
    id = str(id)
    abc = requests.get("https://5sim.net/v1/user/sms/inbox/" + id, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/json"
    })
    jason = json.loads(abc.text)
    OnlyCode = jason["code"]
    return OnlyCode
    #return jason
