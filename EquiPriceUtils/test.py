import requests
from flask import Blueprint, jsonify, request


if __name__ == '__main__':
    url = "http://121.37.39.202:8087/test/getValue2"
    data = {"url": "https://hotels.ctrip.com/hotels/36882921.html#ctm_ref=hp_htl_pt_pro_01"}
    response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        print("请求成功！")
        print(response.json())
    else:
        print(f"请求失败，状态码：{response.status_code}")