# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.forms import forms
from .models import *
# Create your views here.
from django.shortcuts import render, redirect
from .forms import *
from django.db import models
from django.db.models.signals import post_delete


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})

def index(request):
    imgs0 = Upload1.objects.all()
    imgs = []
    for i in imgs0:
        imgs.insert(0,i)
    content={
        'imgs':imgs,
    }
    return render(request, 'new_index.html',content)
def info(request):
    if request.method == 'POST':
        my_form = forms.Form(request.POST, request.FILES)
        if my_form.is_valid():
            new_img = Upload1(
                img = request.FILES.get('img'),
                finder = request.POST.get('finder',''),
                phoneNumber = request.POST.get('phoneNumber',''),
                details = request.POST.get('details',''),
                user = request.user
            )
            new_img.save()
    return render(request, 'info.html')
def opinion(request):
    if request.user.is_superuser:
        s = Suggestion.objects.all()
        slist = []
        index = 0
        for i in s:
            slist.insert(0,i)
            i.index = index
            index+=1
        if request.method == 'POST':
            deletelist = request.POST.getlist('delete')
            if deletelist:
                start = 0
                for i in deletelist:
                    i = int(i)
                    deletelist[start] = slist[i]
                    start+=1
                for i in deletelist:
                    slist.remove(i)
                    i.delete()
                index = 0
                for i in slist:
                    i.index = index
                    index+=1
        content = {'slist':slist}
        return render(request, 'envelope2.html', content)
    else:
        if request.method == 'POST':
            new_suggestion = Suggestion(
                suggestion = request.POST.get('suggestion'),
                user = request.user)
            new_suggestion.save()
        return render(request, 'envelope.html')
def change_information(request):
    return render(request, 'change.html')
def about_us(request):
    return render(request,'about_us.html')    
def delete(request):
    imgs0 = Upload1.objects.all()
    imgs = []
    for i in imgs0:
        imgs.insert(0,i)
    user = request.user
    name = user.username
    Uploadlist = []
    index = 0
    if user.is_superuser:
        for i in imgs:
            i.index = index
            Uploadlist.append(i)
            index+=1
    else:
        for i in imgs:
            if i.user.username==name:
                i.index = index
                Uploadlist.append(i)
                index+=1
    if request.method == 'POST':
        deletelist = request.POST.getlist('delete')
        if deletelist:
            start = 0
            for i in deletelist:
                i = int(i)
                deletelist[start] = Uploadlist[i]
                start+=1
            for i in deletelist:
                Uploadlist.remove(i)
                i.img.delete(save=False)
                i.delete()
            index = 0
            for i in Uploadlist:
                i.index = index
                index+=1
    content = {'Uploadlist':Uploadlist}
    return render(request, 'delete.html', content)
