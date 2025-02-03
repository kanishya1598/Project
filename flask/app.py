from flask import Flask, jsonify, make_response
import json

app = Flask(__name__)


@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route('/services/healthcheck/', methods=["GET"])
def api_healthcheck():
    data = {"application": "GPT QA",
            "health": "ok", "description": "Thanks for checking !!"}
    return json.dumps(data)


@app.route('/services/version/', methods=["GET"])
def api_version():
    data = {"version": "1.0.0", "app": "GPT QA", "env": "dev"}
    return json.dumps(data)


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == "__main__":
    app.run(debug=True)
