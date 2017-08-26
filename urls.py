# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:55:23
# @Author  : lileilei
from handlsers.login_headerl import LoginView,LogoutView
from handlsers.view import IndexView,ShebeiView,UserView,AddShebei,DongjieShebeiView,JieShebeiView
url=[
    ('/login',LoginView),
    ('/logout',LogoutView),
    ('/index',IndexView),
     ('/shebei',ShebeiView),
    ('/shebei/(?P<page>\d*)',ShebeiView),
     ('/user',UserView),
    ('/user/(?P<page>\d*)',UserView),
    ('/addshebei',AddShebei),
    ('/dongjie/(?P<id>\d*)',DongjieShebeiView),
    ('/jie/(?P<id>\d*)',JieShebeiView),
]