#!/usr/bin/env python
#--coding:utf-8--

#无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

def application(environ,start_response):
    start_response("200 ok",[("content-type","text/html")])
    body = "<h1>Hello,%s!</h1>" % (environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf-8")]
