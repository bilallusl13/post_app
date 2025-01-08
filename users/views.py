from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import login,logout

from django.contrib.auth import login as auth_login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Kullanıcıyı giriş yaptır
            messages.success(request, "Successfully logged in!")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("posts:list")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Yeni kullanıcıyı kaydet
            auth_login(request, user)  # Kullanıcıyı oturum açtır
            messages.success(request, "Registration successful! You are now logged in.")  # Başarı mesajı
            return redirect("posts:list")  # Kullanıcıyı yönlendir
        else:
            messages.error(request, "Please correct the errors below.")  # Hata mesajı
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("posts:list")