from django.urls import path
from . import views
urlpatterns = [
path('',views.home, name='My name is vasala Lakshmi supriya'),
path('first/',views.firstpage, name='Regd no - 23B01A12I1'),
path('second/',views.secondpage, name='It -c'),
path('hello/',views.htmlpage, name='hello'),
]
