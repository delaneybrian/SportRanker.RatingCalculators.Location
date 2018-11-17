import pika

from Configuration.Constants import MessagingConstants
from dispatcher import Dispatcher

class Consumer:

    def __init__(self):
        self.dispatcher = Dispatcher()

    def message_callback(self, ch, method, properties, body):
        print("recieved message callback")
        self.dispatcher.recieve_message(method.routing_key, body)

    def start_consumer(self):

        params = pika.URLParameters(MessagingConstants.CLOUD_AMPQ_URL)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.RATING_CHANGE_EXCHANGE,
                                 exchange_type='topic')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=MessagingConstants.RATING_CHANGE_EXCHANGE,
                           queue=queue_name,
                           routing_key=MessagingConstants.TEAM_RATING_CHANGE)

        print(' [*] Waiting for results. To exit press CTRL+C')

        channel.basic_consume(self.message_callback,
                              queue=queue_name,
                              no_ack=True)

        channel.start_consuming()