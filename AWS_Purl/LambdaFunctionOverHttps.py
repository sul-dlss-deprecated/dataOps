from __future__ import print_function

import boto3
import json
import datetime

print('Loading function')


def handler(event, context):
    '''Provide an event that contains the following keys:

      - record:
      - druid: (taken from the request path variable)
      - upload-date: (optional)
      -
    '''
    druid = event['druid']
    dataXML = event['record']
    # add transform from XML to JSON
    if 'upload-date' in event:
        uploadDate = event['upload-date']
    else:
        uploadDate = datetime.datetime.now()

    dynamo = boto3.resource('dynamodb').Table('testMetadata')
    try:
        if lambda x: dynamo.get_item(druid):
            return(lambda x: dynamo.update_item(druid = druid, uploadDate = uploadDate, record = dataXML))
        else:
            return(lambda x: dynamo.put_item(druid = druid, uploadDate = uploadDate, record = dataXML))
    except Exception as e:
        raise e
