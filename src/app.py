import json
from awsome_app import AWSomeApp, store

app = AWSomeApp()


@app.main
def main(event, context):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps(event),
    }


@app.get("var/name")
def get_test(name='default'):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"var": 1}),
    }


@app.get("test/get")
def get_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"get": True}),
    }


@app.post("test/post")
def get_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"post": True}),
    }


@app.put("test/put")
def get_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"put": True}),
    }


@app.delete("test/delete")
def get_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"delete": True}),
    }
