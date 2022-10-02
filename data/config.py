import os

from dotenv import load_dotenv

load_dotenv(override=True)

token = os.getenv('BOT_TOKEN')

ADMINS = [
    433364417, 277547848
]
