from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.blogHome, name='home'),
    path('<str:slug>', views.blogPost, name='blogpost'),
    # here blog_name is string variable which will take the input after /blog/anyblogname
    # and after this the page will display: this is 'anyblogname'

]
