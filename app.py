from flask import Flask, render_template, request
import requests

def call_api(api_url, data):
    response = requests.post(api_url, data=data)
    
    if response.status_code == 200:
        return response.json()["summary"]
    else:
        print("\n\n===RESPONSE===\n"+str(response.text)+"\n")


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.form
        print(type(request.form))
        summary = call_api("http://127.0.0.1:5000/sum", data)
        summary = call_api("http://127.0.0.1:5000/sum", data)

        return render_template("index.html", summary=summary)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
