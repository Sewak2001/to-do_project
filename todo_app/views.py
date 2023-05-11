from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import Todoform
# Create your views here.
#home function
def home(request):
    return render(request,'home.html')

#Signup function
def signup(request):
    if request.method =='POST':
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password==confirm:
            if User.objects.filter(username=user).exists():
                messages.success(request,'user already exists')
                return redirect('sign')

            elif User.objects.filter(email=email).exists():
                messages.success(request,'email already exists')
                return redirect('sign')

            else:
                User.objects.create_user(username=user,email=email,password=password).save()
                return redirect('login')
            
        else:
            messages.success(request,'password not match')
        return render(request,'sign.html')
    return render(request,'sign.html')

#login function
def login(request):
    if request.method =='POST':
        user = request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(username=user,password=password)

        if user is None:
            messages.error(request,'user/password not exist')
            return redirect('sign')
        else:
            auth.login(request,user)
            return redirect('form')

    else:
        return render(request,'login.html') 

#logout function
def logout(request):
    auth.logout(request)
    return redirect('login')



#form function
@login_required(login_url='login')
def form(request):
    if request.method == 'GET':
        form =Todoform()
        return render(request,'form.html',{'form':form})

    else:
        form = Todoform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('show')

        else:
            return redirect('form')

#show function        
@login_required(login_url='login')
def show(request):
    data = TodoItem.objects.all()
    return render(request,'show.html',{'data':data})

#delete function
@login_required(login_url='login')      
def delete(request,id):
    data = TodoItem.objects.get(id=id)
    data.delete()
    return redirect('show')


#Update  function
@login_required(login_url='login')
def update(request,id):
    data = TodoItem.objects.get(id=id)
    if request.method == 'GET':
        form = Todoform(instance=data)
        return render(request,'form.html',{'form':form})

    else:
        form = Todoform(request.POST,instance=data)
        if form.is_valid:
            form.save()
            return redirect('show')
        else:
            return redirect('form')