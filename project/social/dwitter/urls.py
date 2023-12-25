# dwitter/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import dashboard, profile_list, profile,register, logout_request,login_request

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("register/", register, name="register"),
    path('logout_request/', logout_request, name='logout_request'),
    path('login/', login_request, name='login'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)