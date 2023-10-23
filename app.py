from flask import Flask, render_template, request

from config import token
from workApi import Quick

app = Flask(__name__)


@app.route('/')
def hello_world():
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
    app.run(debug=True, host="0.0.0.0", port=8000)
