import sqlite3
from member.service import MemberService
from blood.service import BloodService
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html', name='')

@app.route('/login', methods = ['POST'])
def login():
    print('로그인 들어옴')
    userid = request.form['userid']
    password = request.form['password']
    print("컨트롤러 어이디 {}, 비번 {}".format(userid, password))
    service = MemberService()
    row = service.login(userid, password)
    view = ''
    if row is None:
        view = 'index.html'
    else:
        view = 'main.html'
    return render_template(view)

@app.route('/move/<path>',methods=['GET'])
def move(path):
    print('{}로 이동'.format(path))
    return render_template('{}.html'.format(path))
@app.route('/blood', methods=['POST'])
def blood():
    weight = request.form['weight']
    age = request.form['age']
    print("컨트롤러 어이디 {}, 비번 {}".format(weight, age))
    service = BloodService('data.txt')
    raw_data = service.create_raw_data()
    result = service.make_session(raw_data, weight, age)
    return render_template('blood.html',name = 'result' )
if __name__ == '__main__':
    app.run()
