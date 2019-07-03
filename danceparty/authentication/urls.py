from django.contrib.auth import views as auth_views
from django.urls import path

from authentication import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.UserSignupForm.as_view(), name='signup'),
    path('', (auth_views.LoginView.as_view(template_name='registration/login_form.html')), name='login'),
]
