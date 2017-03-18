import pprint
import requests

API_getRandom = "http://api.petfinder.com/pet.getRandom"
API_get = "http://api.petfinder.com/pet.get"

def getRandom_params(location):

    params = dict()
    params["key"] = yourkey
    params["location"] = location
    params["format"] = "json"

    return params

def get_params(petid):
    params = dict()
    params["key"] = yourkey
    params['id'] = petid
    params['format'] = "json"
    return params

def queryAPI(API_URL, params):

    request = requests.get(API_URL, params = params)
    data = request.json()

    return data

location = "Palo Alto, CA"

params = getRandom_params(location)
randompetID = int(queryAPI(API_getRandom, params)['petfinder']["petIds"]["id"]["$t"])
new_params = get_params(randompetID)
data = queryAPI(API_get, new_params)
pprint.pprint(data)

def makestory(data):
    description = data['petfinder']["pet"]["description"]["$t"]
    pic = data["petfinder"]['pet']["media"]["photos"]["photo"][0]["$t"]

    return description + pic

print(makestory(data))
