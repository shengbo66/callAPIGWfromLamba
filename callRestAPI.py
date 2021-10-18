import json
import requests


print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # print("value1 = " + event['key1'])
    # print("value2 = " + event['key2'])
    # print("value3 = " + event['key3'])
    #raise Exception('Something went wrong')
    i = 1
    while i < 100:
        res = requests.get('https://2zd4e3koo8-vpce-07ab213eeb77f4a5f.execute-api.ap-east-1.amazonaws.com/test/pets?1')
        #print(res.text)
        i += 1
    return event['key1']  # Echo back the first key value
