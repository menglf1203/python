# /usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
import xlwt
import xlrd

class Zhilian():

    def neirong(self,url,head):
        zhiwei=[]
        mingcheng=[]
        jingyan=[]
        xinzi=[]
        riqi=[]
        didian=[]
        renshu=[]

        res=requests.get(url=url,headers=head)
        html=res.content.decode('UTF-8')
        patt=re.compile(r'"jobName":"(.*?)"')
        items=patt.findall(html)
        for i in items:
            zhiwei.append(i)

        patt2=re.compile(r'"url":"(.*?)","size":')
        items2=patt2.findall(html)
        for i in items2:
            i=i.split('"')[-1]
            mingcheng.append(i)

        patt3=re.compile(r'"workingExp":(.*?)"}')
        items3=patt3.findall(html)
        for i in items3:
            i=i.split('"')[-1]
            jingyan.append(i)

        patt4=re.compile(r'"salary":"(.*?)",')
        items4=patt4.findall(html)
        for i in items4:
            xinzi.append(i)

        patt5=re.compile(r'"updateDate":"(.*?)"')
        items5=patt5.findall(html)
        for i in items5:
            riqi.append(i)

        patt6=re.compile(r'"city":{"items":(.*?)"},"')
        items6=patt6.findall(html)
        for i in items6:
            i=i.split('"')[-1]
            didian.append(i)

        patt7=re.compile(r'"size":(.*?)"}')
        items7=patt7.findall(html)
        for i in items7:
            i=i.split('"')[-1]
            renshu.append(i)

        neirong=list(zip(zhiwei,mingcheng,jingyan,xinzi,riqi,didian,renshu))
        return neirong



    def baocun(self,neirong,i):

        f=xlrd.open_workbook('智联招聘2.xls')
        from xlutils.copy import copy
        ff=copy(f)
        sheet=ff.get_sheet(0)
        for j in neirong:
            sheet.write(i, 0, '{}'.format(j[0]))
            sheet.write(i, 1, '{}'.format(j[1]))
            sheet.write(i, 2, '{}'.format(j[2]))
            sheet.write(i, 3, '{}'.format(j[3]))
            sheet.write(i, 4, '{}'.format(j[4]))
            sheet.write(i, 5, '{}'.format(j[5]))
            sheet.write(i, 6, '{}'.format(j[6]))
            i+=1

        ff.save('智联招聘2.xls')


head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
zhilian=Zhilian()
city=[]

tou = ['职位', '公司名称', '经验', '薪资', '发布日期', '工作地点', '人数']
f = xlwt.Workbook(encoding='utf-8')
sheet = f.add_sheet('sheet1')
for i, j in enumerate(tou):
    sheet.write(0, i, '{}'.format(j))
f.save('智联招聘2.xls')

for j in range(0,121,60):
    beijing = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.94273026&x-zp-page-request-id=5baa2e2ffb9c4905acc39245ee706c00-1541813924874-766235'.format(j)
    hangzhou = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.13245989&x-zp-page-request-id=9cbf104ecc954118841bfca470496ca6-1541768374319-213433'.format(j)
    shanghai = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.92987059&x-zp-page-request-id=58b47caf49d444a98342d6d5dfc9d9b7-1541814155773-998722'.format(j)
    city.append(beijing)
    city.append(shanghai)
    city.append(hangzhou)
for i,h in enumerate(city):
    a=zhilian.neirong(h,head)
    zhilian.baocun(a,i*60+1)
print('over')


#2
#
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
#
# aa,bb,cc,dd=[],[],[],[]
# for h in range(0,121,60):
#     url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.45173304&x-zp-page-request-id=0c1565ef76964b7782b8247e2eae1383-1542874194096-716139'.format(h)
#     res=requests.get(url=url,headers=head)
#     html=res.json()
#     for i in range(60):
#         a=html['data']['results'][i]['jobName']
#         b=html['data']['results'][i]['company']['name']
#         c=html['data']['results'][i]['salary']
#         d=html['data']['results'][i]['workingExp']['name']
#         aa.append(a)
#         bb.append(b)
#         cc.append(c)
#         dd.append(d)
#
# neirong=list(zip(aa,bb,cc,dd))
#
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('sheet1')
# sheet.write(0,0,'职位')
# sheet.write(0,1,'公司名称')
# sheet.write(0,2,'薪资')
# sheet.write(0,3,'经验')
# for i,j in enumerate(neirong):
#     sheet.write(i+1,0,'{}'.format(j[0]))
#     sheet.write(i + 1, 1, '{}'.format(j[1]))
#     sheet.write(i + 1, 2, '{}'.format(j[2]))
#     sheet.write(i + 1, 3, '{}'.format(j[3]))
#
# f.save('20181122.xls')


# 3

import json
import requests
import re
import xlwt
import xlrd
import xlutils


class Zhilian():

    def neirong(self,url):
        res=requests.get(url=url)
        html=res.content.decode('utf-8')
        b,c,d,e,f,h,x=[],[],[],[],[],[],[]
        a=json.loads(html)
        for i in range(60):
            b.append(a['data']['results'][i]['jobName'])
            c.append(a['data']['results'][i]['company']['name'])
            d.append(a['data']['results'][i]['workingExp']['name'])
            e.append(a['data']['results'][i]['salary'])
            f.append(a['data']['results'][i]['updateDate'])
            h.append(a['data']['results'][i]['city']['display'])

            k=(a['data']['results'][i]['positionURL'])
            res=requests.get(url=k)
            html=res.content.decode('utf-8')
            patt=re.compile(r'<span><a target="_blank" href="(.*?)</div>',re.S)
            items=patt.findall(html)
            if items==[]:
                x.append('空')
            else:
                x.append(items[0].split('</span>')[-2].replace('<span>','').replace('\n',''))

        aa=list(zip(b,c,d,e,f,h,x))
        return aa
    def baocun(self,aa,i):
        f=xlrd.open_workbook('智联.xls')
        from xlutils.copy import copy
        ff=copy(f)
        sheet=ff.get_sheet(0)
        for j in aa:
            sheet.write(i,0,'{}'.format(j[0]))
            sheet.write(i, 1, '{}'.format(j[1]))
            sheet.write(i, 2, '{}'.format(j[2]))
            sheet.write(i, 3, '{}'.format(j[3]))
            sheet.write(i, 4, '{}'.format(j[4]))
            sheet.write(i, 5, '{}'.format(j[5]))
            sheet.write(i, 6, '{}'.format(j[6]))
            i+=1

        ff.save('智联.xls')

zhilian=Zhilian()
city=[]
tou = ['职位名称','公司','经验','薪资','发布日期','地点','人数']
f = xlwt.Workbook(encoding='utf-8')
sheet = f.add_sheet('sheet1')
for i, j in enumerate(tou):
    sheet.write(0, i, '{}'.format(j))
f.save('智联.xls')

for j in range(0,121,60):
    beijing = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.94273026&x-zp-page-request-id=5baa2e2ffb9c4905acc39245ee706c00-1541813924874-766235'.format(j)
    hangzhou = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.13245989&x-zp-page-request-id=9cbf104ecc954118841bfca470496ca6-1541768374319-213433'.format(j)
    shanghai = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.92987059&x-zp-page-request-id=58b47caf49d444a98342d6d5dfc9d9b7-1541814155773-998722'.format(j)
    city.append(beijing)
    city.append(shanghai)
    city.append(hangzhou)
for i,h in enumerate(city):
    print(h)
    a=zhilian.neirong(h)
    zhilian.baocun(a,i*60+1)
print('over')
