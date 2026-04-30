from flask import Flask, render_template, request
import os

app = Flask(__name__)

# All ruter

@app.route('/')
def hjem():
	return render_template('index.html')

@app.route('/lovverk')
def lovverk():
	return render_template('lovverk.html')

@app.route('/kundesupport')
def kundesupport():
	return render_template('kundesupport.html')

@app.route('/artikkler')
def artikkler():
	return render_template('artikkler.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)