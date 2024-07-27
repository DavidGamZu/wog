from flask import Flask
from utils import score_file_name, bad_return_code

ERROR = bad_return_code
app = Flask(__name__)


@app.route("/")
def index():
    try:
        file = open(score_file_name, 'r')
        score = file.read()
        file.close()
        return f"""<html>
<head>
    <title>Scores Game</title>
</head>
<body>
    <h1>The score is:</h1>
    <div id="score">{score}</div>
</body>
</html>
    """
    except FileNotFoundError:
        return f"""<head>
    <title>Scores Game</title>
</head>
<body>
    <h1>ERROR:</h1>
    <div id="score" style="color:red">{ERROR}</div>
</body>
</html>"""


app.run("0.0.0.0", port=5050)
