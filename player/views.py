from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Song


# def home(request):
#     return render(request, 'player/home.html')
def home(request):
    songs = Song.objects.all()
    return render(request, 'player/home.html', {'songs': songs})


def login_view(request):
    return render(request, 'player/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'player/signup.html', {'form': form})

from django.shortcuts import render

def home(request):
    return render(request, 'player/home.html')

def playlist(request):
    return render(request, 'player/playlist.html')  # Playlist page

def login_view(request):
    return render(request, 'player/login.html')

def signup_view(request):
    return render(request, 'player/signup.html')





# Signup View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'player/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'player/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'player/signup.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('home')  # Replace 'home' with your home view name

    return render(request, 'player/signup.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            return render(request, 'player/login.html', {'error': 'Invalid credentials'})
    return render(request, 'player/login.html')


# Optional Logout View
# def logout_view(request):
#     logout(request)
#     return redirect('login')
from django.shortcuts import render

def test_csrf(request):
    if request.method == "POST":
        return render(request, "player/test_success.html")
    return render(request, "player/test_csrf.html")



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        msg = data.get("message", "").lower()

        if "punjabi" in msg:
            reply = "Try 'DONALI', 'RED ALERT', or 'SO HIGH' 🎵"
        elif "english" in msg:
            reply = "You may like 'Perfect', 'On My Way', or 'Memories' 🎧"
        elif "romantic" in msg:
            reply = "Romantic hits: 'Tum Mile', 'Raabta', 'Tera Ban Jaunga' 💖"
        elif "sad" in msg:
            reply = "Sad list: 'Channa Mereya', 'Tujhe Kitna Chahne Lage' 😢"
        else:
            reply = "Please ask about Punjabi, English, romantic or sad songs 🎶"

        return JsonResponse({"reply": reply})
