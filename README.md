# AWSome-app

## Deploy on AWS

`sam build`

`sam deploy`

## Run local server

`sam build && sam local start-api`

Access on <https://127.0.0.1:3000>

## Test

`sam local invoke "AWSome" -e events/test.json`

## Delete deploy on AWS

`sam delete`
