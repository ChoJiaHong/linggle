from pymongo import MongoClient
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import main_config
mongoDb='local'
mongoCollection='grammar'
_mongodbIp=main_config.mongodbIp
_mongodbPort=main_config.mongodbPort

client = MongoClient(_mongodbIp, _mongodbPort)
db = client[mongoDb]
collection = db[mongoCollection]
