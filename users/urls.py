from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),           
    path('login/', login_view, name='login'),          
    path('logout/', logout_view, name='logout'),       
    path('profile/<int:user_id>/', profile, name='profile'), 
    path('profile/edit/', edit_profile, name='edit_profile'), 
]

