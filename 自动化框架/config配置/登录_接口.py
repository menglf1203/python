# /usr/bin/env python
# -*- coding:utf-8 -*-

import requests


class 学校_查询():
    def 学校_快查(self,city):
        head = {
            'cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        city = {'filterInput': '{}'.format(city)}
        res = requests.get(url=url, headers=head, params=city)
        html = res.json()
        return html

    def 服务器(self,a,b):
        url = "http://192.168.0.57:5000/login"
        payload = {'username': '{}'.format(a), 'password': '{}'.format(b)}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "1a10d802-6edc-4f43-8496-df54fc37bbc1"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        toubu = response.content.decode()
        return toubu

    def haofenshu1(self,a,b):
        url = "http://testsupport-be.haofenshu.com/v1/accounts/session"
        payload = "account={}&password={}".format(a, b)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "20d04552-d6ec-43c0-8d8d-22c5adba170c"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        html = response.json()
        return html

class Appt():
    def apptoubu(self,a):
        url = "http://www.zhaoapi.cn/product/getProductDetail"
        if type(a)==float or type(a)==int:
            querystring = {"pid": "{}".format(int(a))}
        else:
            querystring = {"pid": "{}".format(a.strip())}
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'Postman-Token': "c7722f39-f0a0-4330-bfea-5f67db4dae6f"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        html=response.content.decode()
        return html




