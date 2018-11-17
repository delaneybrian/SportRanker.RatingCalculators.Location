from logger import Logger
from Configuration.Constants import MessagingConstants
import json

class TeamRatingChangedHandler:

    def __init__(self):
        self.logger = Logger()

    def handle(self, message):
        self.logger.log("Team Rating Handler Handling Message")

        message = message.decode(MessagingConstants.ENCODING)

        message_dict = json.loads(message)

        print(message_dict)