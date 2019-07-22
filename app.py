import flask

app = flask.Flask(__name__)

def _get_datapoints():
    return [
        {"name": "data_1", "value": "1"},
        {"name": "data_2", "value": "2"},
        {"name": "data_3", "value": "3"},
    ]

@app.route("/")
def index():
    data = _get_datapoints()
    return flask.render_template("index.html", data=data)

@app.route("/about")
def about():
    return flask.render_template("/about.html")

if __name__ == "__main__":
    app.run(debug=True)