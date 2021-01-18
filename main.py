from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("pdh.html")

app.run(host="0.0.0.0")
