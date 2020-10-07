import logging
import os


class Config(object):

    # Get the database details from environment variables
    DATABASE_USER = os.environ.get('DATABASE_USER')
    DATABASE_ADDRESS = os.environ.get('DATABASE_ADDRESS')
    DATABASE_PORT = os.environ.get('DATABASE_PORT')
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')

    SQLALCHEMY_DATABASE_URI = "postgres://{user}:{password}@{address}:{port}/{database}".format(
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        address=DATABASE_ADDRESS,
        port=DATABASE_PORT,
        database=DATABASE_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STREAM_LOGGING_LEVEL = logging.DEBUG
    FILE_LOGGING_LEVEL = logging.DEBUG
    FLASK_LOG_FILE = 'logs/log.log'
    ROTATING_LOG_FILE_MAX_BYTES = 1024000
    ROTATING_LOG_FILE_COUNT = 10
    LOG_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')