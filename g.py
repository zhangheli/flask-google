import requests
from flask import Flask, request, make_response

### 看美女图片，快去 ioreq.com
app = Flask(__name__)


@app.route("/")
@app.route('/<path:path>')
def handler(path=""):
	resp = requests.request(request.method, "https://www.google.com/" + request.full_path)

	ret = make_response(resp.content)
	ret.headers["content-type"] = resp.headers['content-type']
	return ret


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5050)
