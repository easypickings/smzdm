'''
什么值得买自动签到脚本
'''
import os
import requests
import config
from push import pushplus


class SMZDM_Bot(object):
    def __init__(self):
        self.session = requests.Session()
        # 添加 headers
        self.session.headers = config.DEFAULT_HEADERS

    def load_cookie_str(self, cookie):
        '''为session添加cookie.
        
        Args:
            cookie: 什么值得买登录cookie.
        '''
        self.session.headers['Cookie'] =cookie.encode('utf-8')


    def checkin(self):
        '''签到函数.

        Returns:
            请求响应内容.
        '''
        url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
        rsp = self.session.get(url)
        try:
            result = rsp.json()
            return result
        except:
            return rsp.content


if __name__ == '__main__':
    sb = SMZDM_Bot()
    cookie = os.environ.get('COOKIE') or config.COOKIE
    sb.load_cookie_str(cookie)
    res = sb.checkin()
    print(res)
    TOKEN = os.environ.get('PUSH_PLUS_TOKEN') or config.PUSH_PLUS_TOKEN
    if TOKEN:
        print('检测到PUSH_PLUS_TOKEN, 准备推送')
        title = '什么值得买每日签到' + ('成功' if res.get('error_code') == 0 else '失败')
        pushplus(title=title, content=res, token=TOKEN)
    print('代码完毕')
