from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if request.session.get('name', None) == 'fdm':
        return render(request, 'assets_app/index.html')
    else:
        return redirect('/login/')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'test' and pwd == '123':
            request.session['name']='fdm'
            return redirect('/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'assets_app/login.html')    
