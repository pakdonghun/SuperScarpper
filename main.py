from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

@app.route("/contact")
def pdh():
  return "안녕하세요!"

app.run(host="0.0.0.0")
