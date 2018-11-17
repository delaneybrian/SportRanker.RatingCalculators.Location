from logger import Logger
from Configuration.Constants import MessagingConstants
from Handlers.team_rating_changed_handler import TeamRatingChangedHandler

class Dispatcher:

    def __init__(self):
        self.logger = Logger()
        self.team_rating_change_handler = TeamRatingChangedHandler()

    def recieve_message(self, routing_key, body):

        print("dispatcher recieved")
        split_routing_key = routing_key.split('.')

        if (len(split_routing_key) == 2):
            if (split_routing_key[0] == MessagingConstants.RATINGS
                and split_routing_key[1] == MessagingConstants.TEAMS):
                self.team_rating_change_handler.handle(body)
        else:
            self.logger.log("Invalid message recived")