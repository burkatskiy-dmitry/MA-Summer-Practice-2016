from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    posts = [
        {'title': 'Lorem Ipsum 1', 'body': 'Dolor sit amet'},
        {'title': 'Lorem Ipsum 2', 'body': 'Dolor sit amet'},
        {'title': 'Lorem Ipsum 3', 'body': 'Dolor sit amet'},
        {'title': 'Lorem Ipsum 4', 'body': 'Dolor sit amet'}]
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run()
