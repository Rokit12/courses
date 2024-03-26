from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('finder', views.finder, name='finder'),
    path('details', views.details, name='details'),
    path('certificate', views.earn_certificate, name='certificate'),
    path('account', views.account, name='account'),
]
