class BidirectionalMap:
    def __init__(self):
        self.fir = {}
        self.sec = {}

    # 添加双向映射
    def add(self, key, value):
        if key in self.fir or value in self.sec:
            raise ValueError("映射已存在")
        self.fir[key] = value
        self.sec[value] = key

    # 键 -> 值
    def get_forward(self, key):
        return self.fir.get(key)

    # 值 -> 键
    def get_backward(self, value):
        return self.sec.get(value)

    # 移出映射
    def remove(self, key=None, value=None):
        if key is not None and key in self.fir:
            value_to_remove = self.fir.pop(key)
            del self.sec[value_to_remove]
        elif value is not None and value in self.sec:
            key_to_remove = self.sec.pop(value)
            del self.fir[key_to_remove]
        else:
            raise KeyError("未找到映射")


PLATFORM_LIST = [
    "京东",
    "淘宝",
    "拼多多",
    "携程旅行",
    "美团",
    "东方航空",
    "滴滴出行"
]

PLATFORM_TABLE = BidirectionalMap()

PATH_FOR_DATA = "static/data/"
PATH_FOR_DATA_INDEX = "static/data_index.json"

