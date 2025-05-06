from django.urls import path
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import views

# ✅ Custom logout view
def logout_view(request):
    logout(request)
    return redirect('home')

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('playlist/', views.playlist, name='playlist'),
    path('logout/', logout_view, name='logout'),  # ✅ Added logout here correctly
       path("chatbot/", views.chatbot_response, name="chatbot"),
       
]
