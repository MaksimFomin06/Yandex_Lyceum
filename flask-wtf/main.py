from flask import Flask, request, url_for, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/index/<substitution>")
def index(substitution=None):
    context = {
        "substitution": substitution,
    }
    
    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')