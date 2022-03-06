import requests
import json
from decouple import config


class Api:
    def __init__(self):
        # Below you would replace 'YOUR API KEY' with your actual api key. to get one contact @cameron on the Infinite Flight Community
        self.apikey = 'YOUR API KEY'

        # or you could use this to get the api key from a .env file with the name: .env
        # Then you would put API_KEY='YOUR API KEY'
        self.api_key = config('API_KEY')

    def sessions(self):
        url = requests.get(f'https://api.infiniteflight.com/public/v2/sessions?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def flights(self, serverId):
        #for server id 7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856 = Expert server
        # to get these id's use the sessions function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/flights/{serverId}?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def flight_route(self, flight_id):
        # get flight id from flights function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/flight/{flight_id}/route?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def flight_plan(self, flight_id):
        # get flight id from flights function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/flight/{flight_id}/flightplan?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def ATC(self, serverId):
        #for session id '7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856' = Expert server
        # to get these id's use the sessions function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/atc/{serverId}?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def stats(self, username):
        #IF username

        data_json = {

          "discourseNames": [
            f"{username}"
          ]
        }
        url = requests.post(f'https://api.infiniteflight.com/public/v2/user/stats?apikey={self.apikey}', json=data_json)
        return url.text


    def userGrade(self, userId):
        # To get user id you can get them from the flights function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/user/grade/{userId}?apikey={self.apikey}')
        response = json.loads(url.text)
        return response


    def atis(self, airportIcao, serverId):
        #for server id '7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856' = Expert server
        # to get these id's use the sessions function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/airport/{airportIcao}/atis/{serverId}?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def airport(self, airportIcao, serverId):
        #for server id '7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856' = Expert server
        # to get these id's use the sessions function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/airport/{airportIcao}/status/{serverId}?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def world(self, serverId):
        #for server id '7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856' = Expert server
        # to get these ids use the sessions function

        url = requests.get(f'https://api.infiniteflight.com/public/v2/world/status/{serverId}?apikey={self.apikey}')
        return url.text

    def oceanicTracks(self):
        url = requests.get(f'https://api.infiniteflight.com/public/v2/tracks?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser

    def userFlights(self, userId):
        # To get user id you can get them from the flights function
        url = requests.get(f'https://api.infiniteflight.com/public/v2/user/flights/{userId}?apikey={self.apikey}')
        responser = json.loads(url.text)
        return responser


api = Api()

print(api.sessions())
print(api.flights('SERVER ID'))
print(api.flight_route('FLIGHT ID'))
print(api.flight_plan('FLIGHT ID'))
print(api.ATC('SERVER ID'))
print(api.stats('USERNAME'))
print(api.userGrade('USER ID'))
print(api.atis('AIRPORT ICAO', 'SERVER ID'))
print(api.airport('AIRPORT ICAO', 'SERVER ID'))
print(api.world('SERVER ID'))
print(api.oceanicTracks())
print(api.userFlights('USER ID'))
'''
it is now up to you to filter it all out! 

Make sure to change the parameters when you print the functions!'''


