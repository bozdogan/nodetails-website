import os.path as osp
from flask import Flask, render_template, request
import requests

API_URL = "http://httpbin.org/post"
API_URL = "http://127.0.0.1:5000/sum"

def call_api(api_url, text_body, method, model_name):
    data = {"text": text_body, 
            "method": method,
            "model_name": model_name}
    response = requests.post(api_url, data=data)
    
    if response.status_code == 200:
        return response.json()["summary"]
    else:
        print("\n\n===RESPONSE===\n"+str(response.text)+"\n")


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        text_body = request.form["text"]
        method = request.form["method"]
        model_name = request.form["model_name"]

        summary = call_api(API_URL, text_body, method, model_name)

        return render_template(
            "index.html", text=text_body, summary=summary, choice=method)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
