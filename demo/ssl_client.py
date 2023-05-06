import json
import socket
import ssl

import log
from chat_parameters import ChatParameters
from completions_parameters import CompletionsParameters

logger = log.get_logger('client')

## model 模型和api的对应关系
m = {
    'gpt-4': 'chat',
    'gpt-4-0314': 'chat',
    'gpt-4-32k': 'chat',
    'gpt-4-34k-0314': 'chat',
    'gpt-3.5-turbo': 'chat',
    'gpt-3.5-turbo-0301': 'chat',

    'text-davinci-003': 'completions',
    'text-davinci-002': 'completions',
    'text-curie-001': 'completions',
    'text-babbage-001': 'completions',
    'text-ada-001': 'completions',
    'davinci': 'completions',
    'curie': 'completions',
    'babbage': 'completions',
    'ada': 'completions'
}
salt = '91C10EFA6D054D69BC750AF372D200FA'


class SSLClient:

    def __init__(self): ## 初始化一个ssl socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 创建了一个 SSL上下文,ssl.PROTOCOL_TLS表示选择客户端和服务器均支持的最高协议版本
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # 设置模式为CERT_REQUIRED，在此模式下，需要从套接字连接的另一端获取证书；如果未提供证书或验证失败则将引发 SSLError。
        context.verify_mode = ssl.CERT_REQUIRED
        # 加载一组用于验证服务器证书的CA证书
        context.load_verify_locations("ca.crt")
        self.ssl_sock = context.wrap_socket(s, server_hostname='ai.hapigo.com')
        self.ssl_sock.connect(('ai.hapigo.com', 443))

    def chat(self, parameters: ChatParameters): ## 请求chat接口
        logger.info(f"request parameters {parameters}")
        self.ssl_sock.send(str(parameters).encode())
        res = []
        while True:
            msg = json.loads(self.ssl_sock.recv(1024).decode('utf-8'))
            logger.info(msg)
            delta = msg['choices'][0]['delta']
            if 'content' in delta:
                res.append(delta['content'])

            stop = msg['choices'][0]['finish_reason']
            if stop is not None:
                logger.info('对话结束，关闭')
                break
        all_content = ''.join(res)
        logger.info(f'all content is {all_content}')

    def completions(self, parameters: CompletionsParameters): ## 请求completions接口
        logger.info(f"request parameters {parameters}")
        self.ssl_sock.send(str(parameters).encode())
        res = []
        while True:
            msg = json.loads(self.ssl_sock.recv(1024).decode('utf-8'))
            logger.info(msg)
            text = msg['choices'][0]['text']
            res.append(text)
            stop = msg['choices'][0]['finish_reason']
            if stop is not None:
                logger.info('对话结束，关闭')
                break

        all_content = ''.join(res)
        logger.info(f'all content is {all_content}')
