import boto3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import main_config

_AWS_SERVER_PUBLIC_KEY = main_config.AWS_SERVER_PUBLIC_KEY
_AWS_SERVER_SECRET_KEY = main_config.AWS_SERVER_SECRET_KEY
_dynamodb_region_name = main_config.dynamodb_region_name
_dynamodb_table = main_config.dynamodb_table

session = boto3.Session(
    aws_access_key_id=_AWS_SERVER_PUBLIC_KEY,
    aws_secret_access_key=_AWS_SERVER_SECRET_KEY,
)
dynamodb = session.resource("dynamodb", region_name=_dynamodb_region_name)
grammar = dynamodb.Table(_dynamodb_table)
