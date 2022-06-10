from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def main():
    users = User.get_all()
    return render_template('index.html', users = users)

@app.route('/createuser')
def create():
    return render_template('index2.html')

@app.route ('/users/newuser', methods=['POST'])
def process():
    print(request.form)
    User.save(request.form)
    return redirect('/')

if __name__==('__main__'):
    app.run(debug=True)