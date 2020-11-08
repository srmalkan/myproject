from django.urls import path,reverse_lazy
from .views import dashboard, register,index
app_name = 'account'

urlpatterns = [
    path('',index,name='landing'),
    path('dashboard/',dashboard,name='dashboard'),
    path('register/',register,name='register'),
]
