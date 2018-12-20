from Configuration.Constants import TeamConstants
import requests
from logger import Logger
import json

class DataProvider:

    def __init__(self):
        self.logger = Logger()

    def get_state_and_city_by_team_id(self, team_id):
        url = "https://sports-rivals.appspot.com/api/teams/" + team_id

        result = requests.get(url)

        if (result.status_code == 200):

            team_dict = json.loads(result.text)

            state_url = team_dict["_links"]["state"]['href']
            city_url = team_dict["_links"]["city"]['href']

            state_result = requests.get(state_url)
            city_result = requests.get(city_url)

            if (state_result.status_code == 200 and
                city_result.status_code == 200):

                state_dict = json.loads(state_result.text)
                city_dict = json.loads(city_result.text)

                return state_dict["id"], city_dict["id"]

        else:
            self.logger.info_log("Error Getting Team From Api Id: " + team_id)

    def get_teams_for_city_by_id(self, city_id):

        url = "https://sports-rivals.appspot.com/api/teams/search/findByCity?id=" + city_id

        cities_result = requests.get(url)

        if(cities_result.status_code == 200):
            cities_team_dict = {}
            cities_dict = json.loads(cities_result.text)
            city_teams = cities_dict["_embedded"]["teams"]
            for team in city_teams:
                cities_team_dict[team["id"]] = team["rating"]
            return cities_team_dict
        else:
            self.logger.info_log("Could Not Get Teams For CityId: " + city_id)

    def get_teams_for_state_by_id(self, state_id):

        url = "https://sports-rivals.appspot.com/api/teams/search/findByState?id=" + state_id

        states_result = requests.get(url)

        if (states_result.status_code == 200):
            state_team_dict = {}
            states_dict = json.loads(states_result.text)
            state_teams = states_dict["_embedded"]["teams"]
            for team in state_teams:
                state_team_dict[team["id"]] = team["rating"]
            return state_team_dict
        else:
            self.logger.info_log("Could Not Get Teams For StateId: " + state_id)
