from flask import json

from EquiPriceUtils.CONST import PATH_FOR_DATA, PATH_FOR_DATA_INDEX
import hashlib
import base64

UserInfoList = {}


def get_path(user_account):
    return PATH_FOR_DATA + user_account + ".json"


def hash_password(password):
    hash_object = hashlib.sha256()
    encode_data = password.encode()
    hash_object.update(encode_data)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def new_user(account, password):
    if account in UserInfoList:
        print(account + "已存在,请重试")
        return "error"
    else:
        password_hash = hash_password(password)
        UserInfoList[account] = password_hash
        return "success"


def examine_account(account, password):
    password_hash = hash_password(password)
    if account in UserInfoList:
        if UserInfoList[account] == password_hash:
            return "pass"
        else:
            return "reject"
    else:
        print(account + "未存在,请注册")
        return "error"


def save_to_database(data):
    json_string = json.dumps(data, indent=4)
    with open(PATH_FOR_DATA_INDEX, 'w') as json_file:
        json.dump(data, json_file)


def read_from_database():
    with open(PATH_FOR_DATA_INDEX, 'r') as json_file:
        return json.load(json_file)
