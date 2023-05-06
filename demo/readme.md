## openai-ssl-socket-demo

功能说明
创建一个ssl-socket去请求服务，服务请求chatgpt并流式响应数据

ca.crt 信任证书

chat_parameters chat接口请求参数

completions_parameters   completions接口请求参数

log 自定义的一个log工具

ssl_client client工具类，调用远程服务端

test_ssl_client 测试类

可直接运行，命令行输入
> .venv/bin/python test_ssl_client.py