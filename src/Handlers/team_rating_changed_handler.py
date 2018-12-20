from logger import Logger
from Configuration.Constants import MessagingConstants
import json
from data_provider import DataProvider
from rating_calculator import RatingCalculator
from Configuration.Constants import RankingChangeType
from Configuration.Constants import RankingChangeConstants
from publisher import Publisher

class TeamRatingChangedHandler:

    def __init__(self):
        self.logger = Logger()
        self.data_provider = DataProvider()
        self.rating_calculator = RatingCalculator()
        self.publisher = Publisher()

    def handle(self, message):
        self.logger.info_log("Team Rating Handler Handling Message")

        message = message.decode(MessagingConstants.ENCODING)

        message_dict = json.loads(message)

        team_id = message_dict["Id"]

        team_rating = message_dict["Ranking"]

        state_id, city_id = self.data_provider.get_state_and_city_by_team_id(team_id)

        if(state_id != None and
           city_id != None):

            state_teams = self.data_provider.get_teams_for_state_by_id(state_id)

            new_state_rating = self.rating_calculator.calculate_new_location_rating(team_id, team_rating, state_teams)

            self.logger.info_log("StateId rating: %s changed to %s." % (state_id, new_state_rating))

            state_rating_change_message = {
                RankingChangeConstants.LOCATION_ID: state_id,
                RankingChangeConstants.RANKING: new_state_rating,
                RankingChangeConstants.RANKING_CHANGE_TYPE: RankingChangeType.STATE
            }

            state_rating_change_message_json = json.dumps(state_rating_change_message)

            self.publisher.publish(state_rating_change_message_json, MessagingConstants.LOCATION_RATING_CHANGE)


            city_teams = self.data_provider.get_teams_for_city_by_id(city_id)

            new_city_rating = self.rating_calculator.calculate_new_location_rating(team_id, team_rating, city_teams)

            self.logger.info_log("CityId rating: %s changed to %s." % (city_id, new_city_rating))

            city_rating_change_message = {
                RankingChangeConstants.LOCATION_ID: city_id,
                RankingChangeConstants.RANKING: new_city_rating,
                RankingChangeConstants.RANKING_CHANGE_TYPE: RankingChangeType.CITY
            }

            city_rating_change_message_json = json.dumps(city_rating_change_message)

            self.publisher.publish(city_rating_change_message_json, MessagingConstants.LOCATION_RATING_CHANGE)

        else:
            self.logger.info_log("Could Not Get City Or State For Team: " + team_id)
