import urllib
import os
import sys
import json


def get_terminalinfo():
    key = 'lkZqiljssOIElXPpnwXd'
    url = f'http://api.nubija.com:1577/ubike/nubijaInfoApi.do?apikey={key}'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    if response.getcode() == 200:
        #통신 성공시 처리 -> postman으로 통신 수행 및 응답결과 확인(구조확인)
        #결과는 json -> json 처리하는 모듈 필요
        info = json.load(response)
        print(info)
        pass
    else:
        #통신 실패시 처리
        print('error code', response.getcode())
        return None

    return info['TerminalInfo']