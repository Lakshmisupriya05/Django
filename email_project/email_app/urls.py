from django.urls import path
from .views import send_email_view, home_view
urlpatterns = [
    path('', home_view, name='home'), 
    path('send-email/', send_email_view, name='send_email'),
]

