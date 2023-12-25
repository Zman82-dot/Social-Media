from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from .forms import DweetForm
from django.urls import reverse
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Dweet, Profile
from dwitter.forms import CustomUserCreationForm
# dwitter/views.py

from django.shortcuts import render
from .models import Profile
from .forms import CustomUserCreationForm

# dwitter/views.py
def index(request): 
    return render(request, 'login.html')
@csrf_exempt
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")

    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(request,
        "dashboard.html",
        {"form": form, "dweets": followed_dweets},
    )

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

# dwitter/views.py

# ...

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "profile.html", {"profile": profile})
@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect("dwitter:dashboard")
        else:
            return render(request, "register.html", {"form": form})
@csrf_exempt
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return  redirect('dashboard')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    context={}
    return render(request, 'login.html', context)
       
 