from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)

@babel.localeselector
def get_locale():
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

