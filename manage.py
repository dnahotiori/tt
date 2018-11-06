# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from flask_sqlalchemy import *
from config import *


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = ConfigSite.SQL_Str
    # 动态追踪修改设置，如未设置只会提示警告
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True
    db = SQLAlchemy(app)
    from .View.Home import api as homepage
    app.register_blueprint(homepage, url_prefix="/home/")
    return app

# @app.route("/")
# def homeIndex():
#     value = request.args.get("sss")
#     print(value)
#     # abort(401)
#     return "index"


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="192.168.5.5", port=80)
