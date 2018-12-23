from logger import Logger

class RatingCalculator:

    def __init__(self):
        self.logger = Logger()

    def calculate_new_location_rating(self, team_id, team_rating, ratings_by_team_id):

        total_rating = 0
        num_teams = 0

        for location_team_id, location_team_rating in ratings_by_team_id.items():
            if(location_team_id == team_id):
                continue
            else:
                total_rating += location_team_rating
                num_teams += 1

        total_rating += team_rating
        num_teams += 1

        return total_rating / num_teams