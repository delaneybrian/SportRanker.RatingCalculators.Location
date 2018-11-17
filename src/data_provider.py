from Configuration.Constants import TeamConstants

class DataProvider:

    def get_team_details_by_feed_id(self, feed_provider_id, team_id):
        return {"teamId": 5, "rating": 1500}

    def get_teams_for_location_by_id(self, region_id):
        teams = []

        team1 = {
            TeamConstants.ID: 1,
            TeamConstants.NAME: "Bucks",
            TeamConstants.SPORT_ID: 3,
            TeamConstants.SPORT_NAME: "NBA",
            TeamConstants.STATE_ID: 2,
            TeamConstants.STATE_NAME: "New York",
            TeamConstants.CITY_ID: 4,
            TeamConstants.CITY_NAME: "New York",
            TeamConstants.RATING: 1500,
            TeamConstants.EXTERNAL_MAPPINGS: None,
            TeamConstants.IMAGE_URL: "Fake Image Url"
        }

        teams.append(team1)

        team2 = {
            TeamConstants.ID: 2,
            TeamConstants.NAME: "Sheets",
            TeamConstants.SPORT_ID: 4,
            TeamConstants.SPORT_NAME: "NBA",
            TeamConstants.STATE_ID: 5,
            TeamConstants.STATE_NAME: "California",
            TeamConstants.CITY_ID: 64,
            TeamConstants.CITY_NAME: "LA",
            TeamConstants.RATING: 1500,
            TeamConstants.EXTERNAL_MAPPINGS: None,
            TeamConstants.IMAGE_URL: "Fake Image Url"
        }

        teams.append(team2)

        return teams
