from flask import Blueprint, render_template

from EquiPriceUtils.CONST import PLATFORM_LIST, PLATFORM_TABLE
from EquiPriceUtils.UserInfo import read_from_database

"""
页面映射路由管理
"""
pageCtr = Blueprint('init_bp', __name__)


# /默认index
@pageCtr.route('/')
def page():
    return render_template('index.html')


# homepage主页面
@pageCtr.route('/page_homepage')
def homepage():
    return render_template('EquiPrice/homepage.html')


# detect 杀熟检测
@pageCtr.route('/page_detect')
def detect():
    return render_template('EquiPrice/detect.html')


# law 法律申诉
@pageCtr.route('/page_law')
def law():
    return render_template('EquiPrice/law.html')


# euser 仿真用户
@pageCtr.route('/page_euser')
def euser():
    return render_template('EquiPrice/euser.html')


# serve 服务
@pageCtr.route('/page_serve')
def serve():
    return render_template('EquiPrice/serve.html')


# logout 登出
@pageCtr.route('/page_logout')
def logout():
    return render_template('EquiPrice/logout.html')


@pageCtr.route('/page_login')
def login():
    return render_template('EquiPrice/login.html')