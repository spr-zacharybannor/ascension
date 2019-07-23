import flask
from infrastructure.view_modifiers import response

app = flask.Flask(__name__)

def _get_datapoints():
    return [
        {"name": "data_1", "value": "1"},
        {"name": "data_2", "value": "2"},
        {"name": "data_3", "value": "3"},
    ]

@app.route("/")
@response(template_file="home/index.html")
def index():
    data = _get_datapoints()
    return {"data": data}

@app.route("/about")
@response(template_file="home/about.html")
def about():
    return {}

if __name__ == "__main__":
    app.run(debug=True)