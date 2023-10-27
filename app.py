import flask
from flask import Flask, render_template, request, redirect, url_for, Response
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, login_manager

from config import token, path, name_login, password_login
from db import users, User
from workApi import Quick
import pdfkit
from flask import redirect, url_for, request
from http import HTTPStatus

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


@login_manager.unauthorized_handler
def unauthorized():
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

            id = current_user.id
            user = users.get(id)
            user.data_query = find
            user.type_query = choice
            users.update(user)
            return render_template("index.html", info=info,
                                   info_add_info=info_add_info, info_user=info_user)
        else:
            flask.flash('Нет данных')
    return render_template('index.html')


@app.route(f'/generate-pdf')
@login_required
def download_pdf():
    user = users.get(current_user.id)
    quick = Quick(token)
    info = quick.find(user.type_query, user.data_query)
    info, info_add_info, info_user = info[0], info[1], info[2]
    out = render_template("index.html", info=info,
                          info_add_info=info_add_info, info_user=info_user)

    options = {
        "orientation": "landscape",
        "page-size": "A4",
        "margin-top": "1.0cm",
        "margin-right": "1.0cm",
        "margin-bottom": "1.0cm",
        "margin-left": "1.0cm",
        "encoding": "UTF-8",
    }

    pdf = pdfkit.from_string(out, options=options)

    return Response(pdf, mimetype="application/pdf",
                    headers={"Content-Disposition": "attachment;filename=outfile.pdf"})


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
