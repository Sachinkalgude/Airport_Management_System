from django.urls import path
from .views import sign_up, login_user


urlpatterns = [
    path('sign_up_form/', sign_up, name='signup'),
    path('login_form/', login_user, name='login'),
]
