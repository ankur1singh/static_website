from flask import Flask
from flask import render_template


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'



@app.route('/', methods=('GET', 'POST'))
def index():
    
    return render_template('index.html',)


@app.route('/about', methods=('GET', 'POST'))
def about():
    
    return render_template('about.html',)

@app.route('/detail', methods=('GET', 'POST'))
def detail():
    
    return render_template('detail.html',)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    
    return render_template('contact.html',)

if __name__ == "__main__":

  app.run(debug = True,port=9000)