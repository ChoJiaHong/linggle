from pymongo import MongoClient
import initMongodb
collection=initMongodb.collection
hintWord="ablaze with"
print(list(collection.find({"ngram": {"$regex":hintWord}},{"_id":0,"term":0})))

def findTerm(hintWord):
    return list(collection.find({"term":hintWord},{"_id":0,"term":0}))
def findPattern(hintWord,words):
    return list(collection.find({"term":words[0],"pattern": {"$regex":hintWord}},{"_id":0,"term":0}))
findPattern(hintWord,"ablaze")