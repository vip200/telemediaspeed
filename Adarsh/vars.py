# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = 4857965
    API_HASH = "801abaf29775cf564efd759def571091"
    BOT_TOKEN = "5010315993:AAG5RNiWdN4LepyTgP61DoReM89HoLyUCtg"
    SESSION_NAME = str(getenv('SESSION_NAME', 'telemediaspeed'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = -1001497492623
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = 384403734#int(getenv('OWNER_ID', '384403734'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = 'https://t.me/xbmc19'
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = 'telemediaspeed'
    else:
        ON_HEROKU = False
    FQDN = 'https://telemediaspeed.herokuapp.com'#str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = 'mongodb+srv://yossi7229:Cc200200!@cluster0.vvxkqcq.mongodb.net'#str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = -1001712885478#list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001712885478")).split()))
