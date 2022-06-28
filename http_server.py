#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

#このpyファイルが存在するディレクトリパスを取得します。
#ファイル出力先を絶対パスにすることで、cronからの実行時などにも対応しやすくなります。
script_dir = os.path.abspath(os.path.dirname(__file__))

#本来はログのローテ等を考えるべきですが、簡易サーバなので、
#起動時の日付をファイル名にして、そのファイルにログを書き続けます。
#適宜リブート運用をすれば、１ファイルが超重くなることは避けられます。
#また、Windows,Linuxどちらの環境でも動くように、ファイルセパレータは「os.path.sep」で扱います。
logfilename = script_dir + os.path.sep + 'log_httpserver_' + datetime.now().strftime("%Y%m%d") +'.log'

#ログ出力を簡単に行うため、標準出力の情報を全てログに追記(a)出力することにします。
buffer = 1
# 通常のprintログなどの出力はstdoutです。
sys.stdout = open(logfilename,"a",buffer)
# 127.0.0.1 - - [23/Feb/2018 12:47:09] "GET / HTTP/1.1" 200 - などのアクセスログはstderr側に出力されます。
sys.stderr = open(logfilename,"a",buffer)

#自分自身で試す場合など他者にアクセスさせない場合は、localhostで起動しましょう。
#空白にすれば、ドメイン名やIPアドレスなどで他のマシンからアクセスできます。
#host = 'localhost'
host = ''
port = 80
httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)

#サーバ起動時のログを出力
print(' === Server Start!! === ', datetime.now().strftime("%Y/%m/%d %H:%M:%S") )
print('serving at port', port)
print('logfile = ' + logfilename)

#実際にサーバを起動します。
try:
    httpd.serve_forever()
except:
    print(' === Server Stopped === ', datetime.now().strftime("%Y/%m/%d %H:%M:%S") )
