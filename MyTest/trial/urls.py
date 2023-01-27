from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView


app_name='trial'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('index',views.home,name='index'),
    path('registration',views.register_request,name='registration'),
    path('login',views.login_user,name='login'),
    path('logout',views.login_user,name='logout'),
    path('computer',views.Adding_Computer,name='new computer'),
    path('computer list',views.computer_list,name='computer list'),
    path('delete computer/<int:id>',views.deletecomputer,name='delete computer'),
    path('car',views.Adding_Cars,name='new car'),
    path('car list',views.Cars_list,name='car list'),
    path('delete car/<int:id>',views.deletecar,name='delete car')
    
   
    #path('update car/<int:id>',views.updatecar,name='update car'),
    #path('updatecarrecord/<int:id>',views.updatecarrecord,name='updatecarrecord')
    

]
