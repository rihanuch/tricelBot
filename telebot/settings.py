import os
import json
from dotenv import load_dotenv

load_dotenv("../.env")

PORT = int(os.getenv('PORT', 5000))
TOKEN = os.getenv('BOT_TOKEN')
URL = os.getenv('URL')

############################################################
############## SOCIAL MEDIA SPECIFIC ACCOUNTS ##############

PROXIES = json.dumps({'http': os.getenv('QUOTAGUARD_URL')})

######################## INSTAGRAM ########################

IG_USER = os.getenv('IG_USER')
IG_PWD = os.getenv('IG_PWD')
IG_FILE_LOC = os.getcwd() + '/downloads/instagram/'

############################################################
