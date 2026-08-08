from flask import Flask, redirect , urlf_for

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'hello_world'

@app.route('/home')
def hello_world():
      return 'hello from home'

@app.route('/<name>')
def user(name):
      return f'hello {name}!'

@app.route('/home/test')
def test_world():
      return redirect(urlf_for('hello_home'))

if __name__ == '__main__' :
        app.run(debug = True)
        