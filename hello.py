# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import url_for, abort, render_template, flash
from flask import Flask, request, session, g, redirect
from flask import jsonify   # Ajax



# 各種設定情報を記述
DEBUG = True

# アプリ生成
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



def hello_world():
    return 'mizingiri World!'


@app.route('/')
def show_entries():
    print '__show_entries()__'
    entry = 1
    return render_template('layout.html', entry=entry)


if __name__ == '__main__':
    app.run()
