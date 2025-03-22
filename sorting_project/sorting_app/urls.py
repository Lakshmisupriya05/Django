from django.urls import path
from .views import index, insert_rows,person_list 
urlpatterns = [
    path('', index, name='index'),
    path('insert/', insert_rows, name='insert'),
    path('list/', person_list, name='person_list'),
]
