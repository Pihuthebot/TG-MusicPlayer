import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "!")

contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict("TG-MusicPlayer/VCBot"))
call_py = PyTgCalls(bot)
