import json


## 参数参考 https://platform.openai.com/docs/api-reference/chat/create
class ChatParameters(object):
    
    model: str = None
    messages: list = None
    temperature: float = None
    top_p: float = None
    n: int = None
    stream: bool = None
    stop: str = None
    max_tokens: int = None
    presence_penalty: float = None
    frequency_penalty: float = None
    logit_bias: dict = None
    user: str = None

    encrypt: str = None ## 自定义参数md5加密字符串 用于验证
    timestamp: int = None ## 自定义时间戳 用于验证

    def __init__(self):
        self.max_tokens = 0x3fffffff
        self.temperature = 1
        self.top_p = 1
        self.n = 1
        self.stream = False
        self.presence_penalty = 0
        self.frequency_penalty: float = 0

    def __str__(self):
        return json.dumps(self.__dict__)
