from flask import Blueprint, jsonify

euser_data = Blueprint('euser_data', __name__)


class EuserData:
    def __init__(self):
        self.online_cnt = [11, 11, 8, 11, 11, 11, 7, 11, 11, 11, 11, 11, 9, 11, 11, 8, 11, 11, 9, 11, 11, 11, 11, 11]
        self.work_time = [16, 9, 18, 5, 22, 14, 13, 18, 19, 7, 11, 20, 17, 10, 19, 2, 20, 12, 15, 1, 4, 18, 13, 23]
        self.item_cnt = [2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2]
        self.online_status = ["在线", "在线", "在线", "在线", "在线", "在线", "在线", "在线", "在线", "在线", "在线"]
        self.level = ["普通", "白银", "普通", "铂金", "普通", "铂金", "白银", "普通", "白银", "白银", "白银"]
        self.sex = ["男", "男", "男", "女", "男", "女", "女", "男", "女", "女", "女"]

    def to_dict(self):
        return {
            "online_cnt": self.online_cnt,
            "work_time": self.work_time,
            "item_cnt": self.item_cnt,
            "online_status": self.online_status,
            "level": self.level,
            "sex": self.sex
        }


@euser_data.route('/euser_info', methods=['GET'])
def get_euser_info():
    ret_data = EuserData()
    return jsonify(ret_data.to_dict())
