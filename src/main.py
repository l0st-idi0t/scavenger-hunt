from flask import *
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/robots.txt')
def robots():
    return "User-agent: * <br> Disallow: /dontlookhere"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)