from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import *
from ..misc import *
import bcrypt

def  logReg(request):
    if 'user_id' not in request.session:
        return render(request, 'logReg.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return redirect('/')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    if request.POST['permissions'] == ADMINREGCODE:
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.permissions=24
        toUpdate.save()
        messages.error(request, 'Account created')
        return redirect('/')
    if request.POST['permissions'] == REGCODE:
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.permissions=1
        toUpdate.save()
        messages.error(request, 'Account created')
        return redirect('/')

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            messages.error(request, 'You are now logged in')
            return redirect('/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/login/')