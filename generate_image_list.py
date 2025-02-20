import os
import json

# 定义图片文件夹路径
image_folder = 'pic2'

# 获取文件夹中的所有JPG图片文件名
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

# 将文件名列表保存为JSON文件
with open(os.path.join(image_folder, 'image_list.json'), 'w') as f:
    json.dump(image_files, f, ensure_ascii=False, indent=4)

print("image_list.json 已生成。") 