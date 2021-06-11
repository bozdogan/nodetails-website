import os.path as osp
from flask import Flask, render_template, request

# try:
    # import nodetails as nd
    # from nodetails import ndabs, ndext
# except ImportError:
    # print("nodetails module is not found in the path")
    # quit(1)

# import tensorflow.keras.backend as K; K.clear_session()
# nd.enable_vram_growth()

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    # if request.method == "POST":
        # text_body = request.form["Inputtext"]
        # sum_choice = request.form["sumChoice"]
        # if sum_choice == "ext":
            # summary = ndext.get_summary(text_body, length=7).summary

            # print(ndext.get_summary(text_body, length=7))
        # elif sum_choice == "abs":
            # summary = ndabs.make_inference(model, text_body)
        # else:
            # print("HATA, HATA, HATA!", sum_choice)

        # return render_template(
            # "index.html", text=text_body, summary=summary, choice=sum_choice)
    # else:
        # return render_template("index.html")
    return render_template("index.html")


if __name__ == "__main__":
    # model_dir = "../data/_models"
    # model_name = "nodetails--food_reviews--80-10--None.model"
    # model = ndabs.load_model(osp.join(model_dir, model_name))

    app.run(port=5001, debug=True)
