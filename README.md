## Flask API Technical Sample:

Returns the sum of two numbers in JSON.

Example command:

`curl -X POST http://0.0.0.0:5000/test --data '{"x": 8, "y": 2}' -H 'Content-Type: application/json'`

Returns:
`{
  "sum": 10
}`

### To test this out yourself:
- clone the project with `git clone https://github.com/jasmine-vo/flask-api-tech-sample.git`
- create a virtualenv `virtualenv env`
- activate virtualenv `source env/bin/activate`
- install requirements `pip install -r requirements.txt`
- start the server with `python server.py`
- in a separate terminal, enter the command `curl -X POST http://0.0.0.0:5000/test --data '{"x": 8, "y": 2}' -H 'Content-Type: application/json'`

### Referred to the following Docs:
- http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
- http://flask.pocoo.org/docs/0.12/patterns/apierrors/#registering-an-error-handler