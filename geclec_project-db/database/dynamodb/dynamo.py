from dynamodb import initDynamodb
from boto3.dynamodb.conditions import Key, Attr

grammar = initDynamodb.grammar


def queryPattern(words, hintWord):
    dynamoDict = grammar.query(
        KeyConditionExpression=Key("term").eq(words[0]),
        FilterExpression=Attr("pattern").contains(hintWord),
        ProjectionExpression="pattern,ngram,example",
    )
    return list(dynamoDict["Items"])


def queryTerm(hintWord):
    dynamoDict = grammar.query(
        KeyConditionExpression=Key("term").eq(hintWord),
        ProjectionExpression="pattern,ngram,example",
    )
    return list(dynamoDict["Items"])
