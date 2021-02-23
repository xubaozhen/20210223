
import time

import requests


def sleep(n_secs):
    time.sleep(n_secs)

def get_params():
    return [['登录成功', '8888', '18767169265', 'success']]

def get_token():
    url='http://192.200.3.177:8901/user-login/code/loginOrRegister'
    data={'code':8888,
          'mobile': '18767169265'}
    headers={

    'User-Agent': 'wa ha ha kang you li/1.0.7 (iPhone; iOS 13.4.1; Scale/2.00)',
    'device': 'C85CACF5-663E-484B-A2AA-060CAE6ABF9F',
    'clientPlatform': '2',
    'Content-Type':'application/json;charset=UTF-8',
    'appType':'2',
    'appVersion': '1.2.0'
}
    resp=requests.post(url,json=data,headers=headers)
    try:
        token=resp.json().get('data').get('token')
    except:
        token=''
    return token


def hook_up():
    print('前置执行')
def hook_down():
    print('后置执行down')
def hook_log(value):
    print(value)


def sleep(response, n_secs):
    if response.status_code == 200:  # 接口请求code等于200 则等待n_secs 秒
        time.sleep(n_secs)
    else:  # 接口请求code不等于200 则等待0.5 秒
        time.sleep(0.5)



if __name__ == '__main__':
    #print(get_params())
    print(get_token())
