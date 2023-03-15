import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import main_config
from dynamodb import dynamo
from mongodb import mongodb

database = main_config.database


def getWithTerm(hintWord):
    if database == "mongodb":
        return mongodb.findTerm(hintWord=hintWord)
    elif database == "dynamodb":
        return dynamo.queryTerm(hintWord=hintWord)


def getWithPattern(hintWord, words):
    if database == "mongodb":
        return mongodb.findPattern(hintWord=hintWord, words=words)
    elif database == "dynamodb":
        return dynamo.queryPattern(hintWord=hintWord, words=words)
