from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index() -> 'html':
    return render_template('index.html',
                           user_name="Не зарегистрирован",
                           content="Новости...")

if __name__ == '__main__':
    app.run()