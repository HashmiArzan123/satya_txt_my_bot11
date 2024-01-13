import os

API_ID = API_ID = 22439323

API_HASH = os.environ.get("API_HASH", "e0e203c8be2c2c58b04d0c59fc82f507")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6334241757:AAHo1iSa_LcjP6jbbEO-Wz1H8wp9Oj9tZSk")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6567662829))

LOG = -1002021098463

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6567662829").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


