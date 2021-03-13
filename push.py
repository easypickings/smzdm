import json
import requests
import config


def pushplus(title, content, token, template='html'):
    '''pushplus消息推送.

    Args:
        title: 消息标题.
        content: 具体消息内容，根据不同template支持不同格式.
        token: 用户令牌.
        template: 发送消息模板, html或json.

    Returns:
        JSON格式的请求响应内容.
    '''
    url = 'https://www.pushplus.plus/send'
    body = {
        'token': token,
        'title': title,
        'content': content,
        'template': template
    }
    data = json.dumps(body).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    rsp = requests.post(url, data=data, headers=headers)
    return rsp.json()


if __name__ == '__main__':
    res = pushplus(title='Title',
                   content='Content',
                   token=config.PUSH_PLUS_TOKEN)
    print(res)
