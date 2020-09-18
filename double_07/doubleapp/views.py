from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'index.html')

def loginhome(request):
    return render(request, 'login.html')

def signuphome(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        # 가입된 정보가 있는지

        if user is not None: #가입된 정보가 있을 때
            auth.login(request, user)
            return redirect('home')
        else: #가입된 정보가 없을 때
            errormasg = "잘못 입력하셨습니다."
            return render(request, 'login.html', {'errormasg':errormasg})
    else:
        return redirect('login') #redirect 뒤에는 .html말고 이름으로 적는게 default
    
def signup(request):
    if request.method=='POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')