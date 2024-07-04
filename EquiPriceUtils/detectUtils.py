from flask import Blueprint, request, jsonify

from EquiPriceUtils.image_src import img_str

URLProcessor = Blueprint('URLProcessor', __name__)


class Result:
    def __init__(self):
        self.img = [img_str, img_str, img_str]
        self.sex = ["男", "男", "男", "女", "男", "女", "女", "男", "女", "女", "女"]
        self.level = ["普通", "白银", "普通", "铂金", "普通", "铂金", "白银", "普通", "白银", "白银", "白银"]
        self.item_cnt = [2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2]
        self.price = []
        self.platform = ["携程", "携程", "携程", "携程", "携程", "携程", "携程", "携程", "携程", "携程"]
        self.detect_time = ["2024/7/4 06:00", "2024/7/3 10:30", "2024/7/1 12:45", "2024/6/30 14:00",
                            "2024/6/28 16:00", "2024/6/27 19:00", "2024/6/25 20:00", "2024/6/24 20:40",
                            "2024/6/22 22:00", "2024/6/20 23:25"]
        self.info = ["长春亚泰饭店-大床房", "维也纳国际酒店-大床房", "丽呈东谷酒店-大床房", "哈尔滨巴黎四季酒店-大床房",
                     "达令公馆-大床房", "乌鲁木齐亚馨酒店（德港万达机场）", "JR东日本大都会大饭店东京羽田", "温哥华泛太平洋酒店",
                     "莫洛约日尼酒店", "马尔代夫JW万豪度假酒店"]
        self.product_link = []
        self.max_price = [415, 423, 414, 517, 720, 445, 845, 2868, 399, 10150]
        self.min_price = [368, 386, 325, 453, 621, 359, 761, 2610, 299, 9227]
        self.percent = [0.82, 0.64, 0.45, 0.82, 0.45, 0.18, 0.73, 0.18, 0.73, 0.73]  # 高于平均价格律

    def to_dict(self):
        return {
            'img': self.img,
            'sex': self.sex,
            'level': self.level,
            'item_cnt': self.item_cnt,
            'price': self.price,
            'platform': self.platform,
            'detect_time': self.detect_time,
            'info': self.info,
            'product_link': self.product_link,
            'max_price': self.max_price,
            'min_price': self.min_price,
            'percent': self.percent,
        }


@URLProcessor.route('/url_receive', methods=['POST'])
def receive():
    data = request.get_json()
    url = ""
    platform = ""
    if 'url' in data:
        url = data['url']
    if 'platform' in data:
        platform = data['platform']

    data_ret = detect_processor(url, platform)

    return jsonify(data_ret.to_dict())


# 根据url,platform检测
def detect_processor(url, platform):
    data_ret = Result()
    return Result()
