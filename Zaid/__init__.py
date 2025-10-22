from pyrogram import Client
from config import (
    API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN,
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3,
    STRING_SESSION4, STRING_SESSION5, STRING_SESSION6,
    STRING_SESSION7, STRING_SESSION8, STRING_SESSION9,
    STRING_SESSION10
)
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)

# Will be initialized later
aiosession = None


async def init_aiosession():
    """Initialize aiohttp ClientSession after event loop starts."""
    global aiosession
    if aiosession is None:
        aiosession = ClientSession()


async def close_aiosession():
    """Gracefully close aiohttp ClientSession."""
    global aiosession
    if aiosession and not aiosession.closed:
        await aiosession.close()

# Default API values if not provided
if not API_ID:
    print("WARNING: API ID NOT FOUND USING ZAID API ⚡")
    API_ID = "6435225"

if not API_HASH:
    print("WARNING: API HASH NOT FOUND USING ZAID API ⚡")
    API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
    print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ⚡")

# --- Bot client ---
app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

# --- User clients ---
def make_client(name, session):
    return Client(name=name, api_id=API_ID, api_hash=API_HASH,
                  session_string=session, plugins=dict(root="Zaid/modules"))

sessions = [
    ("one", STRING_SESSION1),
    ("two", STRING_SESSION2),
    ("three", STRING_SESSION3),
    ("four", STRING_SESSION4),
    ("five", STRING_SESSION5),
    ("six", STRING_SESSION6),
    ("seven", STRING_SESSION7),
    ("eight", STRING_SESSION8),
    ("nine", STRING_SESSION9),
    ("ten", STRING_SESSION10),
]

for name, session in sessions:
    if session:
        print(f"Client{name}: Found.. Starting.. 📳")
        clients.append(make_client(name, session))
