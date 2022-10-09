import json
from awsome_app import AWSomeApp, store, GithubHash, UUID

app = AWSomeApp()


@app.main
def main(event, context):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps(event),
    }


@app.get("var/{name}/{other_var}")
def get_test(name:GithubHash, other_var: UUID):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"var": str(name)}),
    }


@app.get("test/get")
def get_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"get": True}),
    }


@app.post("test/post")
def post_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"post": True}),
    }


@app.put("test/put")
def put_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"put": True}),
    }


@app.delete("test/delete")
def delete_test(op1=0):
    return {
        "statusCode": 200,
        'headers': {"content-type": "application/json"},
        "body": json.dumps({"delete": True}),
    }
