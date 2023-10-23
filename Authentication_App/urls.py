from django.urls import path
from .views import sign_up, login_user,user_profile,log_out


urlpatterns = [
    path('sign_up_form/', sign_up, name='signup'),
    path('login_form/', login_user, name='login'),
    path('profile/',user_profile,name='profile_us'),
    path('logout/',log_out,name='logout_user'),
]
