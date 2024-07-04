from flask import Blueprint, request, jsonify

from EquiPriceUtils.CONST import PLATFORM_LIST

HomeProcessor = Blueprint('HomeProcessor', __name__)


@HomeProcessor.route('/init_homepage', methods=['GET'])
def init_data_post():
    ret_data = {"platform_list": PLATFORM_LIST}
    return jsonify(ret_data)
