from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

#custom your email/phone number matched with password
email=""
password=""

client = ZhihuClient()

try:
    client.login(email, password)
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login(email, password, captcha)

    client.save_token('token.pkl')