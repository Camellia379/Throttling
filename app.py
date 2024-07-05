from flask import Flask

from EquiPriceUtils.UserInfo import UserInfoList, read_from_database
from EquiPriceUtils.detectUtils import URLProcessor
from EquiPriceUtils.euser_data_manage import euser_data
from EquiPriceUtils.generate_processor import generateProcessor
from EquiPriceUtils.homepageUtils import HomeProcessor
from EquiPriceUtils.cut_image import cut_img
from EquiPriceUtils.CONST import *
from EquiPriceUtils.page_manage import *

"""
app配置
"""

app = Flask(__name__)

# 注册：页面路由映射管理
app.register_blueprint(pageCtr)
# 注册：主页面homepage路由
app.register_blueprint(HomeProcessor)
# 注册：URL处理
app.register_blueprint(URLProcessor)
# 注册：图片裁剪
app.register_blueprint(cut_img)
# 注册：报告生成
app.register_blueprint(generateProcessor)
# 注册：仿真用户
app.register_blueprint(euser_data)
# # 注册：登录
# app.register_blueprint(loginCtr)

if __name__ == '__main__':
    # 添加软件表
    for i in range(len(PLATFORM_LIST)):
        PLATFORM_TABLE.add(i, PLATFORM_LIST[i])

    # 初始化用户信息
    UserInfoList = read_from_database()

    app.debug = True
    app.run()
