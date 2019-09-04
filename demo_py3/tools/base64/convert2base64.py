# -*- coding: utf-8 -*-    
import base64

# def change_img_as_base64(img_name, type = "jpg"):
#     with open(img_name, 'rb') as f:
#         translate = base64.b64encode(f.read())
#         html = "<img src=\"data:image/jpg;base64,%s\"/>"
#         return translate

# @staticmethod
# def change_base64_as_img(bs64):
#     img_data = base64.b64decode(bs64)
#     #uuid随机生成的不重复字符串
#     img_path = str(Utils.UUID()) + '.jpg'
#     with open(img_path, 'wb') as f:
#         f.write(img_data)
#     return img_path

with open("demo_py3/AI/Img_analyze/img.JPG","rb") as f:  
    # b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())  
    # base64.b64decode(base64data)
    print(base64_data)
    f.close()

with open("demo_py3/tools/base64/jpg.html", "w", 1024, "utf8") as f:
    html = "<img src=\"data:image/jpg;base64,%s\"/>"
    f.write(html % base64_data.decode())

img_path = "demo_py3/tools/base64/revivification.jpg"
with open(img_path, 'wb') as f:
    img_data = base64.b64decode(base64_data)
    f.write(img_data)