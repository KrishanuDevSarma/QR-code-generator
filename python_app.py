# app.py
!pip install Flask

from flask import Flask, render_template, request
from generate_qr_code import generate_qr_code

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    data_to_encode = request.form.get("data")
    output_file_name = generate_qr_code(data_to_encode)
    return render_template("result.html", file_name=output_file_name)

if __name__ == "__main__":
    app.run(debug=True)