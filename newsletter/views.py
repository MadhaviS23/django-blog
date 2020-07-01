from .models import signup
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.models import User, auth

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.create_user(email = email)
        new_signup = user.email
        user.save()
        return redirect('blog')