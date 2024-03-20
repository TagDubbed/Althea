from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 26739167))
    API_HASH = env.get("TELEGRAM_API_HASH", "9bcf49d320560e6623dc4764a666d8e0")
    OWNER_ID = int(env.get("OWNER_ID", 1019675595))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "1019675595").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Althea_Lucy_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6818014525:AAGQFjMNkIPV3sT21C94fkrhi2Z2Oy97WQA")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001990139196))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://tagkdrama-90d4542058b6.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
