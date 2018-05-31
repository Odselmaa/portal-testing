from flask import Flask
from flask import Response
from flask import stream_with_context
from flask import request
import requests

app = Flask(__name__)
USER_ROOT_URL = "https://portal-user.herokuapp.com/"


@app.route('/<path:url>', methods=["GET", "POST"])
def home(url):
    print(url)
    req = send_request(USER_ROOT_URL + url, request.method, request.json)
    return Response(stream_with_context(req.iter_content()), status=req.status_code,  content_type = req.headers['content-type'])


def send_request(URL, method, data={}):
    global result
    if method == 'GET':
        result = requests.get(URL,  stream = True)
    elif method == 'POST':

        result = requests.post(URL,  stream = True, json=data)
    elif method == 'PUT':
        result = requests.put(URL,  stream = True)
    elif method == 'DELETE':
        result = requests.delete(URL,  stream = True)
    return result


if __name__ == '__main__':
    app.run(port=5005)