import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "I'm awake"

if __name__ == "__main__":
    app.run()