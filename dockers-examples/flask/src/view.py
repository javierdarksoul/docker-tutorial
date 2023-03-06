from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return {"status": 200}


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6001))
    app.run(debug=True, host='0.0.0.0', port=port)