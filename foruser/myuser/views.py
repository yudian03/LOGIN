from django.shortcuts import render,redirect
from .models import myuser
from .forms import *
import hashlib
# Create your views here.
def register(request):
    if request.session.get('is_login',None):
        return redirect("/user/home/")
    if request.method =='POST':
        register_form = Registerform(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 =register_form.cleaned_data['password1']
            password2 =register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex =register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request,"myuser/register.html",locals())
            else:
                db_user = myuser.objects.filter(username = username)
                if db_user:
                    message = "用户名已经存在"
                    return render(request,"myuser/register.html",locals())
                db_email = myuser.objects.filter(email = email)
                if db_email:
                    message = "邮箱地址已经被使用，请更换新的邮箱地址！"
                    return render(request,"myuser/register.html",locals())
                new_user = myuser()
                new_user.username = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/user/home/')
    register_form = Registerform()
    return render(request,'myuser/register.html',locals())

def login(request):

    if request.session.get('is_login',None):
        return  redirect('/myuser/home/')

    if request.method == "POST":
        login_form = Userform(request.POST)
        #username = request.POST.get('username',None)
        #password = request.POST.get('password',None)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
        #if username and password:
            #username = username.strip()
            try:
                user = myuser.objects.get(username = username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/user/home/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在"
        #return render(request,"myuser/login.html",{"message":message})
        return render(request, "myuser/login.html", locals())
    login_form = Userform()
    return render(request,'myuser/login.html',locals())

def home(request):
    pass
    return render(request,'myuser/home.html')
def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/user/home/')

    request.session.flush()
    return redirect("/user/home/")

def hash_code(s,salt='myuser'):
    h =hashlib.sha256()
    s = s+salt
    h.update(s.encode())
    return h.hexdigest()
