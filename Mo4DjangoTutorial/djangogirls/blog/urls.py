from django.urls import path 
# . means current folder
from . import views

urlpatterns = [
    #patht that takes in 3 arguments - path url (/pagename), function
    path('', views.post_list, name ='post_list'),
    path('post/<int:pk>,', views.post_detail,name ='post_detail'),
    ]