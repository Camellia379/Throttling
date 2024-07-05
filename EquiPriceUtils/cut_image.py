from flask import Flask, request, jsonify, Blueprint
import base64
import io
from PIL import Image

cut_img = Blueprint('cut_img', __name__)

class Coord:
    def __init__(self, sx, ex, sy, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

def convert_base64_to_image(base64_str):
    img_data = base64.b64decode(base64_str)
    image_stream = io.BytesIO(img_data)
    img = Image.open(image_stream)
    return img

def convert_image_to_base64(image, img_format):
    buffer = io.BytesIO()
    image.save(buffer, format=img_format)
    img_str = buffer.getvalue()
    img_base64 = base64.b64encode(img_str)
    img_base64_str = img_base64.decode('utf-8')
    return img_base64_str

def cut_image(img, coords):
    cut_images = []
    for coord in coords:
        cropped_img = img.crop((coord.sx, coord.sy, coord.ex, coord.ey))
        cut_images.append(convert_image_to_base64(cropped_img, 'PNG'))
    return cut_images

@cut_img.route('/cut_image', methods=['POST'])
def cut_image_route():
    data = request.get_json()
    base64_img = data.get('base64Image')  # 提取键名为 base64Image 的数据

    area = [
        Coord(200, 431, 46, 514),
        Coord(200 + 239, 431 + 239, 46, 514),
        Coord(200 + 239 * 2, 431 + 239 * 2, 46, 514),
        Coord(200 + 239 * 3, 431 + 239 * 3, 46, 514),
        Coord(200 + 239 * 4, 431 + 239 * 4, 46, 514),
        Coord(200 + 239 * 5, 431 + 239 * 5, 46, 514),
        Coord(200 + 239 * 6, 431 + 239 * 6, 46, 514),

        Coord(200, 431, 46 + 475, 514 + 475),
        Coord(200 + 239, 431 + 239, 46 + 475, 514 + 475),
        Coord(200 + 239 * 2, 431 + 239 * 2, 46 + 475, 514 + 475),
        Coord(200 + 239 * 3, 431 + 239 * 3, 46 + 475, 514 + 475),
        Coord(200 + 239 * 4, 431 + 239 * 4, 46 + 475, 514 + 475),
        Coord(200 + 239 * 5, 431 + 239 * 5, 46 + 475, 514 + 475),
        Coord(200 + 239 * 6, 431 + 239 * 6, 46 + 475, 514 + 475),
    ]

    img = convert_base64_to_image(base64_img)
    cut_images_base64 = cut_image(img, area)
    return jsonify(cut_images_base64)

if __name__ == '__main__':
    cut_img.run(debug=True)
