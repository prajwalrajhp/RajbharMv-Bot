import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Movieprovider')
API_ID = int(environ.get('API_ID', '14175941'))
API_HASH = environ.get('API_HASH', '95c18a1b2ab8d932a95c15182ac2323d')
BOT_TOKEN = environ.get('BOT_TOKEN', "5408155242:AAF-PUTEumPuWX1Eyc1z2YTQ0Q0rZNWRSZk")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/4b2852ca00781d2e454e9.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/363a1d552aac5aabc46d7.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/b60d2facc538ad82ad22d.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/d25f2895cb100c5c1c6f4.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1511468725 5494151843 5838674798').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', ' -1001840476165').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1511468725 5494151843 5838674798').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('')
auth_grp = environ.get('')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://nejot19048:R8dtclyDQVaL@cluster0.x5cbzoh.mongodb.net/? retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "crezyboter")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', 'https://telegram.me/mvisland')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Movies_island8')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/RajbharMvSupport')
MSG_ALRT = environ.get('MSG_ALRT', 'Share and Support Us')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', -1001885372079))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL',  -1001840476165))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', '')
HOW_DWLD_LINK = environ.get('HOW_DWLD_LINK', 'https://t.me/mvisland/428')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001928522177))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', -1001928522177))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '<b>@rajbharmv_bot {file_name}\n\n\n{file_size} </b>')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>{mention}'s Qᴜᴇʀʏ ☞ <code>{query}</code>\n\n<b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n💀 Rᴇʟᴇᴀsᴇ :  <b>{release_date}</b> <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>#{genres}</b></b>\n\n<b>🔅 Pᴏᴡᴇʀᴇᴅ Bʏ : {message.chat.title}</b>")
CYNITE_IMDB_TEMPLATE = environ.get("CYNITE_IMDB_TEMPLATE", "<b><b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n💀 Rᴇʟᴇᴀsᴇ :  <b>{release_date}</b> <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>{genres}</b></b>\n\n<b>📖 Sᴛᴏʀʏ Lɪɴᴇ :</b> <code>{plot}</code>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Auto Delete , Filter & Auto Filter
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
SPL_DELETE_TIME = int(environ.get('SPL_DELETE_TIME', 5))

# URL SHORTNER

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'tinyfy.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '3f73b17a7be21f6141e82ce9f76cddb61f386f2e')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
