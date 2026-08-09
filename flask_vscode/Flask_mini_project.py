from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

#set  a secret key for encrypting session data
app.secret_key = 'my_secret_key'

# dictionary to store user and password 
user = {
    'Aryan' : '12345',
    'user2' : 'password2'
}

# To render a login page
@app.route('/')
def view_form():
    return render_template('login.html')

# for handling get request form we can get
# the form inputs value by using arg attribute.
# this value after submittinng you will see in the urls.
# this exploits our credentials so that's
# why developers prefer post request

@app.route('/handle_get', methods = ['GET'])
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in user and user[username] == password :
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1> invalid credentials!</h1>'

    else:
        return render_template('login.html')

# For handling post request form we can get the form 
#inputs value by using Post attribute.
# This value after submtting you will never see in the urls.

@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username =request.form['username']
        password =request.form['password']
        print(username,password)
        if username in user and user[username] == password:
            return '<h1> Welcome!!!</h1>'
        else:
            return '<h1> invalid credentials!</h1>'

    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run() 