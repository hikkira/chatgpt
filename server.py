from flask import Flask, Response
import ssl

# 服务器配置
hostname = 'localhost'
port = 8080
certfile = 'server.crt'
keyfile = 'server.key'

# 创建 Flask 应用程序实例
app = Flask(__name__)

# 注册路由
@app.route('/')
def index():
    def generate():
        for i in range(10):
            yield f'This is chunk {i}\n'

    return Response(generate(), content_type='text/plain', headers={'Transfer-Encoding': 'chunked'})

# 启动服务器
if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    app.run(host=hostname, port=port, ssl_context=context)
