import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from config import token, path, name_login, password_login
from db import users, User
from workApi import Quick

app = Flask(__name__)
app.secret_key = 'qwdvioknghe4352ncuIK*asde'

login_manager = LoginManager()
login_manager.init_app(app)


class UserFlask(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    user_flask = UserFlask()
    user_flask.id = user_id
    return user_flask


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        id = users.get_id_by_name(name)
        user = users.get(id)
        if name == user.name and password == user.password:
            user_flask = UserFlask()
            user_flask.id = id
            login_user(user_flask)
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
        else:
            flask.flash('Нет данных')
    return render_template('index.html')


@app.route(f'/admin')
@login_required
def admin_panel():
    id = current_user.id
    name = request.args.get("name")
    password = request.args.get("password")
    del_name = request.args.get("del_name")
    admin_id = users.get_id_by_name(name_login)
    admin = users.get(admin_id)
    admin.name = name_login
    admin.password = password_login
    users.update(admin)
    if id in users:
        user = users.get(id)
        if user.name == name_login and user.password == password_login:
            if name and password:
                id = len(users) + 1
                user = User(id=id, name=name, password=password)
                users.add(user)
                flask.flash(f'Пользователь {name} добавлен')
                return redirect(url_for('admin_panel'))
            elif del_name:
                id = users.get_id_by_name(del_name)
                users.del_instance(id)
                flask.flash(f'Пользователь {del_name} удален')
                return redirect(url_for('admin_panel'))
            return render_template('admin.html')
    return "Unauthorized"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
