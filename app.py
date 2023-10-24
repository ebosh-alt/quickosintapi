from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

from config import token, path, name_login, password_login
from workApi import Quick

app = Flask(__name__)
app.secret_key = 'qwdvioknghe4352ncuIK*asde'

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if name == name_login and password == password_login:
            user = User()
            user.id = 1
            login_user(user)
            return redirect(url_for("api"))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route(f'/{path}')
@login_required
def api():
    find = request.args.get("find")
    choice = request.args.get("choice")
    quick = Quick(token)
    if find and choice:
        info = quick.find(choice, find)
        if info:
            info, info_add_info, info_user = info[0], info[1], info[2]
            return render_template("index.html", info=info,
                                   info_add_info=info_add_info, info_user=info_user)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
