from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 22449337))
    API_HASH = env.get("TELEGRAM_API_HASH", "18b1c9675fe7dc9048d8bcd38a87c5af")
    OWNER_ID = int(env.get("OWNER_ID", 6346189744))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "cdnindexbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7436905134:AAGtlT9TS22FeFdhbxF-305DEXcDBr76IGw")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002382049868))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 6))

class Server:
    BASE_URL = env.get("BASE_URL", "https://idfc.koyeb.app")
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
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
