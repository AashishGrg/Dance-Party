from django.urls import path

from dancepartyapp import views

app_name = 'dancepartyapp'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('join_dance_party/<int:pk>/', views.join_dance_party, name='join_dance_party'),
    path('leave_dance_party/<int:pk>/', views.leave_dance_party, name='leave_dance_party'),
]
