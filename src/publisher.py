import pika
from Configuration.Constants import MessagingConstants
from logger import Logger
import time

class Publisher:

    def __init__(self):
        self.logger = Logger()

    def publish(self, message, routing_key):

        params = pika.URLParameters(MessagingConstants.CLOUD_AMPQ_URL)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params)

        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.RATING_CHANGE_EXCHANGE,
                                 exchange_type='topic')

        channel.basic_publish(exchange='topic_logs',
                              routing_key=routing_key,
                              body=message)

        self.logger.info_log(" [x] Sent %r:%r" % (routing_key, message))
        connection.close()

        #time.sleep(5)