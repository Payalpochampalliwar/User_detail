from django.shortcuts import render, redirect
from django.http import Http404
from .models import User

def home(request):
    return render(request, 'users/home.html')

# /hello Route
def hello_world(request):
    return render(request, 'hello.html')

# /users Route
def list_users(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

#new_user Route
def new_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        User.objects.create(name=name, email=email, role=role)
        return redirect('/users')
    return render(request, 'users/new_user.html')

#/users_id Route
def user_details(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("User not found")
    return render(request, 'users/detail.html', {'user': user})
