from django.shortcuts import render, redirect
from django.contrib import messaes
from ..models import *

def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, "Protected Page")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        