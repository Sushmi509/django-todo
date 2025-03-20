from django .urls import path
from . import views

urlpatterns=[
    path('log',views.login_,name='login'),
    path('reg',views.register,name='register'),
    path('logout',views.logout_,name='logout'),
]