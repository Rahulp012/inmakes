from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo1,name='demo1')
    # path('about/',views.about,name='about'),
    # path('welcome/',views.welcome,name='welcome'),
    # path('contact/',views.contact,name='wel'),
    # path('result/',views.result,name='wel1')
    #path('result/',views.mul,name='wel12')

]
