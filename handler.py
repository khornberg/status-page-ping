import json
from ping import get


def main(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps(get())
    }
    return response
