from flask import Flask, render_template

app = Flask("a")

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/draw/')
def draw():
  print ('I got clicked!')