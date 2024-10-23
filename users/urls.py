from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),            # URL for user registration
    path('login/', login_view, name='login'),          # URL for user login
    path('logout/', logout_view, name='logout'),       # URL for user logout
    path('profile/<int:user_id>/', profile, name='profile'),  # URL for viewing user profile
    path('profile/edit/', edit_profile, name='edit_profile'),  # URL for editing user profile
]

