import sys
from flask import Flask, render_template, request
import requests
import json

def call_api(api_url, data):
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("\n\n===RESPONSE===\n"+str(response.text)+"\n")


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.form
        response = call_api(API_URL + "/sum", data)

        text = ""
        text_display = ""
        summary = ""
        extended_summary = ""

        if response:
            if "reference" in response:
                # NOTE(bora): Either extractive or integrated engine here

                text_display = []
                for k, v in response["sentences"].items():
                    text_display.append(f'<a class="referenced" name="ref{k}">{v}</a>')
                text_display = " ".join(text_display)

                sum_linked = []
                for ref in response["reference"]:
                    sum_linked.append(f'<a href="#ref{ref}">{response["sentences"][ref]}</a>')
                extended_summary = " ".join(sum_linked)

                if response["engine"] == "integrated-engine":
                    summary = response["summary"]
            elif "summary" in response:
                summary = response["summary"]
                text = data["text"]
        else:
            text = "Server unavailable"

        return render_template("index.html",
                               text=text,
                               summary=summary,
                               extended_summary=extended_summary,
                               text_display=text_display)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    API_URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5000"
    print("API URL: %s\n" % API_URL)
    
    app.run(port=5001, debug=True)
