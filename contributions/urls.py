from django.urls import path
from . import views

app_name = 'contributions'
urlpatterns = [
    path('', views.home, name='nyumbani'),
    path('Makusanyo', views.source, name='income'),
    path('matumizi', views.expenses, name='expenditure'),

#     login
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]
