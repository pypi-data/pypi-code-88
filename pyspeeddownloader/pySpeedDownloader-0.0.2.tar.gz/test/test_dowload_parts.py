import requests
# 待下载部分的文件起始位置
start = 0
# 待下载部分的文件终止位置
end = 1000
# 每次读取的大小
chunk_size = 128
# 记录下载的位置
seek = start
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
# 这是核心！设定下载的范围
headers['Range'] = f'bytes={start}-{end}'
# 下载链接
url = 'https://github.com/github/gitignore/archive/refs/heads/master.zip'
file_name = 'gitignore-master.zip'
response = requests.get(url, headers=headers, stream=True)

for chunk in response.iter_content(chunk_size=chunk_size):
    _seek = min(seek+chunk_size, end)
    print(f'下载: {seek}-{_seek}')
    seek = _seek
