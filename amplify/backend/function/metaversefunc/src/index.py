import json

import awsgi
import boto3
import os
from flask_cors import CORS
from flask import Flask, jsonify, request

dynamodb_client = boto3.client("dynamodb", region_name="us-east-2")
app = Flask(__name__)
CORS(app)

TABLE = "tenant-staging"
ITEM_ROUTE = "/items"

#@app.route(ITEM_ROUTE, methods=['GET'])
#def list_items():
#    return jsonify(message="hello world!!")

'''
@app.route(ITEM_ROUTE, methods=['POST'])
def create_tenant():
    print(request)
    request_json = request.get_json()
    #client.put_item(TableName=TABLE, Item={
    #    'tenantid': {request_json.get("tenantid")},
    #})
    #return jsonify(message="tenant created")
'''

def handler(event, context):
    print('received event:')
    print(event)
    if event['httpMethod'] == 'POST':
        print("Yes, post")
        #print(event['queryStringParameters']['tenantid'])
        #print(TABLE)
        dynamodb_client.put_item(
            TableName=TABLE,
            Item={
                'tenantid': {'N': event['queryStringParameters']['tenantid']},
                'tenant_industry': {'S': event['queryStringParameters']['tenant_industry']}
            })
    elif event['httpMethod'] == 'GET':
        print("Yes, get")
        response = dynamodb_client.get_item(
            TableName=TABLE,
            Key={
                'tenantid': {'N': event['queryStringParameters']['tenantid']},
                'tenant_industry': {'S': event['queryStringParameters']['tenant_industry']}
            })
        print(response['Item'])
        return {
            "statusCode": 200,
            "body": json.dumps({"tenant": response['Item']})
        }

    return awsgi.response(app, event, context)

'''
def handler(event, context):
  print('received event:')
  print(event)
  
  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello from your new Amplify Python lambda!')
  }
'''