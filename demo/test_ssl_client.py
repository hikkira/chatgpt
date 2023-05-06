import datetime
from hashlib import md5
from unittest import TestCase

from chat_parameters import ChatParameters
from completions_parameters import CompletionsParameters
from ssl_client import SSLClient


def test_completions():
    parameters = CompletionsParameters()

    parameters.model = 'text-davinci-003'
    parameters.prompt = 'say this is a test'
    parameters.stream = True
    parameters.max_tokens = 500

    parameters.timestamp = int(datetime.datetime.now().timestamp())
    parameters.encrypt = md5((str(parameters.timestamp) + '91C10EFA6D054D69BC750AF372D200FA').encode()).hexdigest()

    cl = SSLClient()
    cl.completions(parameters)

def test_chat():
    parameters = ChatParameters()

    parameters.model = 'gpt-3.5-turbo'
    parameters.messages = [
        {"role": "user", "content": "请详细介绍一下opencv"}
    ]
    parameters.stream = True
    parameters.max_tokens = 500

    parameters.timestamp = int(datetime.datetime.now().timestamp())
    parameters.encrypt = md5((str(parameters.timestamp) + '91C10EFA6D054D69BC750AF372D200FA').encode()).hexdigest()

    cl = SSLClient()
    cl.chat(parameters)

## completions
# test_completions()
## chat
test_chat()

