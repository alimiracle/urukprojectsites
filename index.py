from flask import * 
from flask_babel import *

app = Flask(__name__)
babel = Babel(app)
app.config.from_object('config')

@babel.localeselector
def get_locale():
    return g.get('current_lang', app.config['BABEL_DEFAULT_LOCALE'])

@app.route('/dist')
def dist():
    return render_template('distro.html', current_lang = app.config['BABEL_DEFAULT_LOCALE'])

@app.route('/contribute')
def contribute():
    return render_template('contribute.html', current_lang = app.config['BABEL_DEFAULT_LOCALE'])

@app.route('/change_language', methods = ['POST', 'GET'])
def change_language():
    if request.method == 'POST':
            app.config['BABEL_DEFAULT_LOCALE'] = app.config['LANGUAGE'][request.form['lang']]
            return redirect(request.referrer)

@app.route('/')
def index():
    return render_template('index.html', current_lang = app.config['BABEL_DEFAULT_LOCALE'])
    
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=4000)