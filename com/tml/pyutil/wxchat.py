import itchat
import requests


def get_respoinse(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': 'dc3586d008f14d4ea7a301b02247f6c1',
        'info': msg,
        'userId': '暴走的耗子'
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')


@itchat.msg_register(itchat.content.TEXT)  # 用于接收来自朋友间的对话消息
def print_content(msg):
    return get_respoinse(msg['Text'])


#@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)  # 用于接收群的对话消息
#def print_content(msg):
 #   return get_respoinse(msg['Text'])


itchat.auto_login(True)
itchat.run()
