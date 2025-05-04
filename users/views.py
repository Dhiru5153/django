from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404



def hello_world(request):
    return HttpResponse("Hello, World!")

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect after saving
    else:
        form = UserForm()
    return render(request, 'new_user.html', {'form': form})

def user_list(request):
    users = User.objects.all()  # Get all users
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'user_detail.html', {'user': user})