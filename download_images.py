import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 创建保存图片的文件夹
os.makedirs('pic2', exist_ok=True)

# 定义要下载的页面范围
start = 2025024
end = 2025000

# 遍历每个页面
for i in range(start, end, -1):
    # 根据规则选择下载的页面
    if str(i).endswith('3'):
        url = f"https://fuliba2025.net/{i}.html/3"
    else:
        url = f"https://fuliba2025.net/{i}.html/2"
    
    print(f"正在处理: {url}")
    
    # 发送GET请求获取网页内容
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"无法访问 {url}: {e}")
        continue

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有的<img>标签
    img_tags = soup.find_all('img')

    # 下载每个图片
    for img in img_tags:
        img_url = img.get('src')
        if img_url and img_url.endswith('.jpg'):
            # 构造完整的图片URL
            full_url = urljoin(url, img_url)
            
            # 获取图片内容
            try:
                img_response = requests.get(full_url)
                img_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"无法下载图片 {full_url}: {e}")
                continue
            
            # 获取图片名称
            img_name = os.path.basename(img_url)
            
            # 将图片保存到pic2文件夹
            with open(os.path.join('pic2', img_name), 'wb') as f:
                f.write(img_response.content)
            
            print(f"已下载 {img_name}")

print("所有图片下载完成。")