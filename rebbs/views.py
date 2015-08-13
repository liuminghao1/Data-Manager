#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rebbs.forms import LoginForm
import redis
import datetime
from rebbs.userSystem import usSystem

r = redis.StrictRedis(host='localhost',port='6379',db=0)

def index(request):
	art = {}
	if request.user.is_authenticated():
		art['form'] =  "ok"
	return render(request,"rebbs/index.html",art)



def usLogin(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            us = form.cleaned_data['us']
            pwd= form.cleaned_data['pwd']
            if r.exists('us:%s:id' %us):        # 检查是否存在该用户关系键值
                uid = r.get('us:%s:id' %us)     # 获取该用户在user表中对应的id
                if r.exists('user:%s' %uid):    # 检查是否存在该用户键值(如user:1)
                    us_, pwd_ = r.hmget('user:%s' %uid, 'username', 'pwd')  # 获取该用户的用户名密码
                    if us_ == us and pwd_ == pwd:   # 校验成功
                        r.hincrby('user:%s' %uid, 'login_count', 1)     # 登陆次数累加
                        r.hset('user:%s' %uid, 'last_login_date', datetime.datetime.now())  # 添加最近登陆
                        # set Cookies
                        res = HttpResponseRedirect('/rebbs')
                        ussys = usSystem(request, res, uid)
            #            if ussys.testCookie():
                        if ussys.testCookie() and ussys.setCookieAndSession():
           #             if ussys.setCookieAndSession():
				return res
	    context['us'] = us
	    context['pwd'] = pwd		
        context['msg'] = u'账号或密码错误'
        context['form'] = form

    request.session.set_test_cookie()
    form = LoginForm()
    context['form'] = form
    return render(request, 'rebbs/login.html', context)	
