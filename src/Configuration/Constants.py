class MessagingConstants:
    ENCODING = 'utf-8'

    CLOUD_AMPQ_URL = r'amqp://lhqadfns:Ox1Z9RVKMsu36ZjbLV0HEzknWsgJi36S@raven.rmq.cloudamqp.com/lhqadfns'
    HOST = 'localhost'
    PORT = ''

    NEW_FIXTURE_EXCHANGE = 'new_fixture_exchange'
    NBA_RESULTS = 'results.nba'
    NFL_RESULTS = 'results.nfl'
    NHL_RESULTS = 'results.nhl'
    MLB_RESULTS = 'results.mlb'
    ALL_RESULTS = 'results.*'

    RESULTS = 'results'
    NBA = 'nba'
    NFL = 'nfl'
    NHL = 'nhl'
    MLB = 'mlb'

    RATINGS = 'ratings'
    TEAMS = 'team'
    LOCATIONS = 'location'

    RATING_CHANGE_EXCHANGE = 'rating_change_exchange'
    TEAM_RATING_CHANGE = 'ratings.team'
    LOCATION_RATING_CHANGE = 'ratings.location'
    ALL_RATINGS_CHANGE = 'ratings.*'