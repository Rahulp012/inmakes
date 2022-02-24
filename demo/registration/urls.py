from . import views
from django.urls import path

urlpatterns = [



    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout')
    # path('welcome/',views.welcome,name='welcome'),
    # path('contact/',views.contact,name='wel'),
    # path('result/',views.result,name='wel1')
    #path('result/',views.mul,name='wel12')

]
