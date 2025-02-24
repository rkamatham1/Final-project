import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Print the current working directory to verify Flask's location
    print("Current working directory:", os.getcwd())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
