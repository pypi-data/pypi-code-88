# 导入requests 库
import requests
# 文件下载直链
url = 'https://github.com/github/gitignore/archive/refs/heads/master.zip'
file_name = 'gitignore-master.zip'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
print('正在下载文件......')
# 发起请求
response = requests.get(url, headers=headers)

content = response.content

# 以 wb 的模式打开文件
with open(file_name, mode='wb') as f:
    # 写入响应内容
    f.write(content)
print(f'文件下载成功！文件名 {file_name}')
