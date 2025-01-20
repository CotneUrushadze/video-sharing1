from django.urls import path 
from profiles.views import ProfileView

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    
]