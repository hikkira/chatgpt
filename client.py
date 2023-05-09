import ssl
from urllib import request

# 创建了一个 SSL上下文,ssl.PROTOCOL_TLS表示选择客户端和服务器均支持的最高协议版本
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# # 设置模式为CERT_REQUIRED，在此模式下，需要从套接字连接的另一端获取证书；如果未提供证书或验证失败则将引发 SSLError。
context.verify_mode = ssl.CERT_REQUIRED
# # 加载一组用于验证服务器证书的CA证书
context.load_verify_locations("ca.crt")


url = "https://localhost:8080/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

req = request.Request(url, headers=headers)

# 获取响应对象，设置stream参数为True
resp = request.urlopen(req, timeout=5, context=context)

# 逐块读取响应内容
while True:
    chunk = resp.read(1024)
    if not chunk:
        break
    # 处理每个数据块
    print(chunk)
    print()

