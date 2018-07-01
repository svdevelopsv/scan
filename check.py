#!/usr/bin/env python3
import cgi
import random
import time
import requests

start_time = time.time()
#   замена заголовка под браузер случайного типа
headers = {}
headers[0] = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
headers[1] = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
headers[2] = {'User-Agent': 'Opera 12.17 (Win 8 x64): Opera/9.80 (Windows NT 6.2; WOW64) Presto/2.12.388 Version/12.17'}
headers[3] = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; Media Center PC 6.0; CMNTDFJS; F9J; InfoPath.3; rv:11.0) like Gecko'}
headers[4] = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
h = round(random.random() * (len(headers) - 1))

sources = {}
sources[0] = {'url': 'https://egrinf.com/search?q=', 'criteria': 'результатов: 0</h1>'}
sources[1] = {'url': 'https://sbis.ru/contragents/', 'criteria': '<title>Нет данных,'}
sources[2] = {'url': 'https://www.egripegrul.ru/inn/', 'criteria': 'Не найдено, попробуйте еще раз'}
sources[3] = {'url': 'https://demo.logistpro.su/Egr/Search?query=', 'criteria': ':[]}'}
sources[4] = {
    'url': 'https://xn--c1aubj.xn--80asehdb/%D0%BB%D1%8E%D0%B4%D0%B8/?%D1%84%D0%B0%D0%BC%D0%B8%D0%BB%D0%B8%D1%8F=&%D0%B8%D0%BC%D1%8F=&%D0%BE%D1%82%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE=&%D0%B8%D0%BD%D0%BD=',
    'criteria': '<h2>Введите ФИО человека или ИНН</h2>'}
sources[5] = {'url': 'http://www.postavshhiki.ru/proverka-postavshhika?inn=', 'criteria': 'Показано: 0 из 0'}

form = cgi.FieldStorage()
inn = form.getfirst("check", "nothing")
res = ''
for i in range(len(sources)):
    page = requests.get(sources[i]['url'] + inn, headers=headers[h])
    if page.text.find(sources[i]['criteria']) > 0:
        res = 'false'
    else:
        res = 'true'
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
# print(headers[h])
print("--- %s seconds ---" % (time.time() - start_time))
print('   ')
print(res)
print("""</body>
        </html>""")
